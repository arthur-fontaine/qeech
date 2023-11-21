import { useRoute, RouteProp } from '@react-navigation/native';
import { useQuery } from '@tanstack/react-query';
import { Main, ScrollView, YStack, Image, Text } from 'tamagui';

import { Container, Subtitle, Title } from '../../tamagui.config';
import { RootStackParamList } from '../navigation';
import { api } from '../utils/api';

type RecipeScreenNavigationProps = RouteProp<RootStackParamList, 'Recipe'>;

export default function Recipe() {
  const route = useRoute<RecipeScreenNavigationProps>();

  const { recipeId } = route.params;

  const { data: recipe } = useQuery({
    queryKey: ['recipe'],
    queryFn: async () => {
      const recipe = await api.getRecipe(recipeId);
      const recipeImage = await api.getRecipeImage(recipeId);

      return {
        ...recipe,
        image_url: recipeImage.recipe_image_url,
      };
    },
  });

  return (
    <ScrollView>
      <Container>
        <Main>
          <YStack>
            <Image source={{ uri: recipe?.image_url }} width="100%" height={200} />
            <Title>{recipe?.name}</Title>
            <Subtitle>Ingredients</Subtitle>
            {recipe?.ingredients.map((ingredient, i) => <Text key={i}>{ingredient.name}</Text>)}
          </YStack>
        </Main>
      </Container>
    </ScrollView>
  );
}
