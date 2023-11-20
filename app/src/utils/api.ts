import Constants from 'expo-constants';
import * as valibot from 'valibot';

import { useAuthStore } from '../stores/auth-store';

const { manifest2 } = Constants;

if (process.env.NODE_ENV !== 'development') {
  // TODO: Implement API_URL for production
  throw new Error('API_URL is not implemented for production');
}

const HOST_URI = manifest2?.extra?.expoClient?.hostUri;
const API_URL = `http://${HOST_URI?.split(':')[0]}:8000`;

const query = <Schema extends valibot.BaseSchema>(
  url: string,
  body: any,
  schema?: Schema
): Promise<valibot.Output<Schema>> => {
  const { token } = useAuthStore.getState();

  return fetch(`${API_URL}${url}`, {
    method: 'POST',
    body: JSON.stringify(body),
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
  })
    .then((res) => res.json())
    .then((res) => {
      if (schema === undefined) {
        return res;
      }

      return valibot.parse(schema, res);
    });
};

export const api = {
  login(username: string, password: string) {
    return query(
      '/login',
      { username, password },
      valibot.object({
        token: valibot.string(),
      })
    );
  },
};
