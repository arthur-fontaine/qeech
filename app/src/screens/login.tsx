import { useNavigation } from '@react-navigation/native';
import { StackNavigationProp } from '@react-navigation/stack';
import { useMutation } from '@tanstack/react-query';
import { useState } from 'react';
import { Button, Input } from 'tamagui';

import { Container, Main } from '../../tamagui.config';
import { RootStackParamList } from '../navigation';
import { useAuthStore } from '../stores/auth-store';
import { api } from '../utils/api';

type LoginScreenNavigationProps = StackNavigationProp<RootStackParamList, 'Login'>;

export default function Login() {
  const navigation = useNavigation<LoginScreenNavigationProps>();
  const { setToken } = useAuthStore();

  const [identifiers, setIdentifiers] = useState({
    username: '',
    password: '',
  });

  const login = useMutation({
    mutationFn: ({ username, password }: { username: string; password: string }) =>
      api.login(username, password),
    onSuccess: ({ token }) => {
      setToken(token);
      navigation.navigate('Home');
    },
  });

  return (
    <Container>
      <Main>
        <Input
          onChangeText={(username: string) => setIdentifiers({ ...identifiers, username })}
          placeholder="Username"
          defaultValue={identifiers.username}
        />
        <Input
          onChangeText={(password: string) => setIdentifiers({ ...identifiers, password })}
          placeholder="Password"
          defaultValue={identifiers.password}
          secureTextEntry
        />
        <Button
          onPress={() => {
            login.mutate(identifiers);
          }}>
          Login
        </Button>
      </Main>
    </Container>
  );
}
