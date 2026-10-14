# Load Test Results and Deployment Assessment

## Project
Auspify Data Science Internship — Netflix Dashboard

## 1. Test Scope

- Load testing tool: Grafana k6 v2.2.0
- Application: Streamlit dashboard
- Endpoints tested:
  - Dashboard homepage (/)
  - Streamlit health endpoint (/_stcore/health)
- Test type: HTTP endpoint testing
- Limitation: These tests do not simulate full browser rendering, interactive charts, filters, downloads, or complete Streamlit WebSocket sessions.

## 2. Local Load Test — 20 Virtual Users

### Configuration
- Environment: Local
- Maximum virtual users: 20
- Duration: Approximately 5 minutes

### Results

| Metric | Result | Threshold | Status |
|---|---:|---:|---|
| Average HTTP response time | 3.77 ms | Informational | Recorded |
| 95th percentile response time | 10.21 ms | < 500 ms | PASS |
| Maximum HTTP response time | 29.25 ms | Informational | Recorded |
| Failed HTTP requests | 0% | < 1% | PASS |
| Total HTTP requests | 2,098 | Informational | Recorded |
| Successful checks | 4,196 / 4,196 | All pass | PASS |

The local test passed both configured thresholds.

## 3. Local Load Test — 50 Virtual Users

### Configuration
- Environment: Local
- Maximum virtual users: 50
- Duration: Approximately 8 minutes

### Results

| Metric | Result | Threshold | Status |
|---|---:|---:|---|
| Average HTTP response time | 3.79 ms | Informational | Recorded |
| 95th percentile response time | 12.63 ms | < 500 ms | PASS |
| Maximum HTTP response time | 165.84 ms | Informational | Recorded |
| Failed HTTP requests | 0% | < 1% | PASS |
| Total HTTP requests | 7,610 | Informational | Recorded |
| Successful checks | 15,220 / 15,220 | All pass | PASS |

The local test passed both configured thresholds. These results apply only to the tested HTTP endpoints and do not establish the maximum capacity of the complete dashboard.

## 4. Cloud Smoke Test

### Configuration
- Environment: Streamlit Community Cloud
- Test type: Low-volume HTTP smoke test
- Test script: cloud_smoke_test.js

### Recorded Results

An initial smoke test completed 10 HTTP requests with zero failures. Its average response time was 606.65 ms and p95 was 771.29 ms.

A subsequent short test recorded:
- 25 HTTP requests
- Average response time: 587.95 ms
- p95 response time: 728.25 ms
- HTTP failures: 0%
- Checks: 20 / 20 passed

A separate 30-second low-volume smoke test encountered one homepage connection timeout:
- HTTP requests: 10
- Failed requests: 1 (10%)
- p95 response time: 854.6 ms
- Checks: 4 / 6 passed
- The health endpoint returned HTTP 200.
- The failed request reported a connection timeout to the cloud host.

The timeout could reflect transient network or hosting behavior; the available results do not establish its root cause. The cloud tests are inconsistent and do not justify a claim of reliable cloud performance under load.

### Cloud Test Conclusion

The public dashboard was observed loading and its visible filters, charts, and download interactions were previously checked manually. However, cloud HTTP latency was materially higher than local latency, and one short smoke test encountered a timeout. Repeat cloud tests and browser-level checks are recommended before making reliability or capacity claims.

## 5. Hosting and Architecture Assessment

### Hosting provider
- Provider: Streamlit Community Cloud
- Application framework: Streamlit
- Deployment source: GitHub repository
- Public dashboard URL: https://auspify-data-science-internship-58qojsenn592eyhjbut46g.streamlit.app/

### Data and state
- The dashboard reads the cleaned CSV file from the project outputs directory.
- No database connection or database connection pooler is currently used.
- CSV downloads are generated in memory.
- No database writes are part of the described dashboard workflow.
- This architecture reduces database connection and persistent-storage dependencies.
- Full session-state and multi-user isolation behavior has not been independently audited.

### Hosting limits
The exact CPU, memory, concurrency, request-duration, bandwidth, and storage limits applicable to this deployed app have not been established from the available test results. Verify current limits in the hosting provider's official documentation and app settings before capacity planning. Do not infer a supported user count from local HTTP tests.

## 6. Three Likely Failure Points and Mitigations

### 1. Hosting resource saturation or slow cold starts
Potential impact: Slow responses, restarts, or timeouts during periods of increased traffic.

Mitigation:
- Repeat low-volume cloud smoke tests at different times.
- Measure actual browser load and interactive response times.
- Inspect application logs and hosting metrics when available.
- Reduce unnecessary data processing during each rerun and cache expensive computations where appropriate.

### 2. Missing, incorrectly packaged, or unexpectedly large data files
Potential impact: The app may fail during startup or data loading if its expected CSV file is absent or its schema changes.

Mitigation:
- Keep the cleaned CSV in the repository at the expected path.
- Validate file existence and required columns at startup.
- Show a clear error message if data validation fails.
- Test deployment from a clean checkout.

### 3. Streamlit session or WebSocket interruptions
Potential impact: A user may see a disconnected session or lose the current interactive view even when basic HTTP endpoints respond.

Mitigation:
- Perform browser-based tests of filters, charts, downloads, and reconnect behavior.
- Avoid relying on unverified persistent session state.
- Keep important data reproducible from the underlying CSV and filter selections.
- Review hosting logs when disconnects occur.

## 7. Monthly Cost Assessment

The current deployment uses Streamlit Community Cloud, and no separate database service is configured.

A verified monthly cost cannot be calculated from the available evidence because the applicable hosting plan, usage limits, and any paid services have not been documented. Confirm the current provider pricing and whether this specific deployment incurs charges. Do not treat unverified free-tier availability or quotas as guaranteed.

Potential future costs include paid hosting, monitoring, external storage, or a database if the architecture changes. None is established as a current project expense by the information available here.

## 8. Scaling Recommendation

The local tests show that the two tested HTTP endpoints handled the tested workloads without request failures. They do not measure full dashboard concurrency or prove that cloud hosting can support the same workload.

Do not introduce Kubernetes or Amazon ECS based on these results alone. First establish a real need through cloud measurements, browser-level load tests, resource metrics, and documented availability requirements. For this CSV-based dashboard, validate the existing hosting setup before adding infrastructure complexity.

## 9. Final Assessment

- Local HTTP tests at 20 and 50 virtual users passed their configured thresholds.
- Cloud smoke tests showed higher and variable latency.
- One short cloud test experienced a homepage connection timeout.
- Full browser and WebSocket load behavior remains unverified.
- Exact hosting quotas and monthly costs remain to be confirmed.
- No database pooler is needed for the current architecture because no database connection is configured.
- Further cloud validation is required before claiming a production capacity or reliability level.
