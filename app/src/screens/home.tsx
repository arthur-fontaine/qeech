import { useNavigation } from '@react-navigation/native';
import { StackNavigationProp } from '@react-navigation/stack';
import { Text } from 'tamagui';

import { Container, Main } from '../../tamagui.config';
import { RootStackParamList } from '../navigation';
import { useAuthStore } from '../stores/auth-store';

type HomeScreenNavigationProps = StackNavigationProp<RootStackParamList, 'Home'>;

export default function Home() {
  const navigation = useNavigation<HomeScreenNavigationProps>();

  const { token } = useAuthStore();

  return (
    <Container>
      <Main>
        <Text>{token}</Text>
      </Main>
    </Container>
  );
}
