import http from 'k6/http';
import { check, sleep } from 'k6';

const BASE_URL = __ENV.BASE_URL || 'http://127.0.0.1:8501';

export const options = {
  stages: [
  { duration: '30s', target: 5 },
  { duration: '1m', target: 5 },

  { duration: '30s', target: 10 },
  { duration: '1m', target: 10 },

  { duration: '30s', target: 20 },
  { duration: '1m', target: 20 },

  { duration: '30s', target: 50 },
  { duration: '2m', target: 50 },

  { duration: '1m', target: 0 },
],

  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
  // 1. Open the dashboard
  const home = http.get(`${BASE_URL}/`);

  check(home, {
  'dashboard returns HTTP 200': (r) => r.status === 200,

  'dashboard returns HTML': (r) =>
    r.headers['Content-Type'] &&
    r.headers['Content-Type'].includes('text/html'),

  'dashboard response is not empty': (r) =>
    r.body && r.body.length > 0,
});

  sleep(1);

  // 2. Check Streamlit server health
  const health = http.get(`${BASE_URL}/_stcore/health`);

  check(health, {
    'health endpoint returns HTTP 200': (r) => r.status === 200,
  });

  sleep(2);
}