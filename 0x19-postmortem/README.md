## Issue Summary:
From 8:30 PM service started to be unresponsive, leading to request failure till service was completely down at 10 PM. Root cause is invalid change for caching system, forgetting to set the expiration date. The service started to be slow and unresponsive till reached sever level and the and outage occurred with complete loss of service.
## Timeline:
08:30: issue was detected by the monitoring alert, reporting unresponsiveness
11:30: found root cause related to bad implementation for caching clearance and case got resolved.
## Root cause and resolution must contain:
The responsible team the found root cause, revising changes done in the last couple of month, found missing required testing cases and incorrect changes applied and changed rolled back.
And the steps, that the team needed to follow to fix the problem included:
1-	The responsible team received an alert from the monitoring system due to unresponsiveness and possible outage.
2-	The software engineer started revising the error logs and crash report for a possible memory leakage in the site. There report usually contain indicator on what went wrong and serves as a component to find the real reason for the problem at hand.
3-	The relevant team also needed to analyze users report to get complete idea about the situation.
4-	The root cause was identified as a memory leakage caused by cashing failure for not setting the right expiration dates.
5-	A new fix was applied by the software engineering team, and that included modifying the codebase to get the error completely fixed.
6-	The software engineering team need to set more test cases
7-	The code got deployed after fix by the software engineering team and a period of monitoring was applied on the behavior of the software after the fix to ensure no problem is found.
## Corrective and preventative measures must contain:
Team agreed on revisiting the caching implementation. And we decided on the following strategy to be implemented as soon as possible:
1-	Revisiting cashing implementation. Creating separate component for caching to make sure it’s easier for revisions.
2-	Implementing automated testing with scenarios for memory leaks and caching expiration.
3-	Regular review processing set through meetings at the beginning of each month.
4-	Providing documentations and trainings: a documentation regarding setting expiration for the cached data should be applied and the team should be stressed on the importance of such procedures and how they should be applied to prevent such cases in the future.

## Author
Ahmed Elsaeed
