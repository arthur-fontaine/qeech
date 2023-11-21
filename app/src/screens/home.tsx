import { useNavigation } from '@react-navigation/native';
import { StackNavigationProp } from '@react-navigation/stack';
import { useQuery } from '@tanstack/react-query';
import { Pressable } from 'react-native';
import { Text, YStack, Image, ScrollView } from 'tamagui';

import { Container, Main } from '../../tamagui.config';
import { RootStackParamList } from '../navigation';
import { api } from '../utils/api';

type HomeScreenNavigationProps = StackNavigationProp<RootStackParamList, 'Home'>;

export default function Home() {
  const navigation = useNavigation<HomeScreenNavigationProps>();

  const { data: recipe_recommendations } = useQuery({
    queryKey: ['recipe_recommendations'],
    queryFn: async () => {
      const recipe_recommendations = await api.getRecipeRecommendations();

      return await Promise.all(
        recipe_recommendations.recommended_recipes.map(async (recipe_recommendation) => {
          const recipe = await api.getRecipeImage(recipe_recommendation.id);

          return {
            ...recipe_recommendation,
            image_url: recipe.recipe_image_url,
          };
        })
      );
    },
  });

  const onRecipeClick = (recipe_id: number) => {
    navigation.navigate('Recipe', { recipeId: recipe_id });
  };

  return (
    <ScrollView>
      <Container>
        <Main>
          <YStack gap={24}>
            {recipe_recommendations?.map((recipe_recommendation) => (
              <Pressable
                key={recipe_recommendation.id}
                onPress={() => onRecipeClick(recipe_recommendation.id)}>
                <Container backgroundColor="#fff">
                  <YStack>
                    <Image
                      source={{ uri: recipe_recommendation.image_url }}
                      width="100%"
                      height={200}
                    />
                    <Text>{recipe_recommendation.name}</Text>
                  </YStack>
                </Container>
              </Pressable>
            ))}
          </YStack>
        </Main>
      </Container>
    </ScrollView>
  );
}
