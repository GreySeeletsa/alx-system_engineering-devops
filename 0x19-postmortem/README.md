## Postmortem
# Issue Summary
On April 15, 2023, from 2:00 PM to 4:00 PM (EAT), our web application experienced an outage. During this period, approximately 35% of our users were unable to access the service. The root cause was identified as a misconfiguration in our load balancer.

# Timeline
2:00 PM: The issue was first detected when our monitoring system alerted us to a spike in server errors.
2:10 PM: Our engineering team began investigating the issue, initially suspecting a problem with the application code.
2:30 PM: After reviewing recent code deployments and finding no issues, the team started investigating the infrastructure.
3:00 PM: The team identified the load balancer as the potential source of the problem.
3:30 PM: The issue was confirmed to be a misconfiguration in the load balancer.
3:45 PM: The misconfiguration was corrected.
4:00 PM: Service was fully restored.

# Root Cause and Resolution
The root cause of the issue was a misconfiguration in the load balancer that was incorrectly routing traffic to a subset of our servers. This caused those servers to become overloaded and respond with errors. The issue was resolved by correcting the configuration and redistributing the traffic evenly across all servers.

# Corrective and Preventative Measures
To prevent this issue from happening again, we need to improve our infrastructure management and monitoring. Specifically, we should:
  -Implement more robust health checks for our load balancers.
  -Improve our alerting system to catch misconfigurations.
  -Provide additional training for our team on managing and troubleshooting our infrastructure.
  -Here are the tasks we plan to undertake:

# Update our monitoring system to include checks for load balancer configuration.
Review and update our alerting rules to ensure we are notified of similar issues in the future.
Schedule a training session for the engineering team on best practices for managing our infrastructure.
We apologize for any inconvenience caused and appreciate your understanding as we work to improve our service.

!(https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.zenduty.com%2Fblog%2Fblameless-postmortems%2F&psig=AOvVaw0x2Qh1QlfX6I-Lznp0RHnu&ust=1703357766812000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOCN3bHco4MDFQAAAAAdAAAAABAY)
