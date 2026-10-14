import http from 'k6/http';
import { check, sleep } from 'k6';

const BASE_URL = __ENV.BASE_URL || 'http://127.0.0.1:8501';

export const options = {
  vus: 1,
  duration: '30s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
  const home = http.get(`${BASE_URL}/`);
  check(home, {
    'dashboard returns HTTP 200': (r) => r.status === 200,
    'dashboard returns HTML': (r) =>
      r.headers['Content-Type'] &&
      r.headers['Content-Type'].includes('text/html'),
  });

  const health = http.get(`${BASE_URL}/_stcore/health`);
  check(health, {
    'health endpoint returns HTTP 200': (r) => r.status === 200,
  });

  sleep(1);
}
