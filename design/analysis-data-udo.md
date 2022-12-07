# UDO Call Type Analysis 

UDO_conditioned.request table is used to analyze the number of calls received between August 1, 2021, and July 31, 2022, under each category (udo_typename)  and subcategory (udo_subtypename). 

Raw data used for the analysis, SQL query and related summary are in this [file](https://dvagov.sharepoint.com/:x:/r/sites/VoiceBot/Shared%20Documents/General/Data%20and%20Access/Data%20Analysis/crm_udo_typename_Aug21_july22.xlsx?d=wccf08434e2924dfeb64087f8eb1e318c&csf=1&web=1&e=cye4zo). 

## Overview of Findings
Our analysis confirms that claim related calls make up a large portion of calls answered by the agent. Claim related calls account for 41.60% of total call received. Out of which 86.16% of calls were related to General Status, followed by Document verification at 4.38%.  

The results, ordered in descending order, are shown in the following table:

| udo\_typename                        | Sum of Call ID (sum) |
| ------------------------------------ | -------------------- |
| Claim                                | 41.60%               |
| Correspondence and Forms             | 13.61%               |
| General Benefits Information for VBA | 10.71%               |
| Update Information                   | 9.36%                |
| Payments / Debts                     | 6.41%                |
| Dependent Maintenance                | 4.79%                |
| FOIA/Privacy Act                     | 3.39%                |
| FNOD                                 | 2.45%                |
| General Benefits Information for VHA | 1.64%                |
| BVA Appeal                           | 1.60%                |
| Appeals                              | 1.50%                |
| Appeals Modernization                | 0.53%                |
| Supervisor Escalation                | 0.42%                |
| va.gov                               | 0.39%                |
| Contract Examinations                | 0.28%                |
| eBenefits                            | 0.27%                |
| Non VA Calls                         | 0.23%                |
| Ghost Call/Disconnected Call         | 0.21%                |
| Fiduciary                            | 0.17%                |
| General Benefit Information For NCA  | 0.15%                |
| Special Issues                       | 0.12%                |
| Potential Incident                   | 0.04%                |
| Novel Coronavirus                    | 0.04%                |
| SEP/VSO                              | 0.04%                |
| Eligibility Determinations           | 0.02%                |
| Hurricane                            | 0.01%                |
| OTH Discharge                        | 0.00%                |
| Sensitive File                       | 0.00%                |
| Mission Act                          | 0.00%                |
| Life Insurance                       | 0.00%                |
| Suicide Call                         | 0.00%                |
| Media Inquiries                      | 0.00%                |
| RAMP                                 | 0.00%                |
| Threat Call                          | 0.00%                |
| New VA Letter                        | 0.00%                |
| Grand Total                          | 100.00%              |

The further breakdown of the category which received the highest number of calls - Claim is shown in the table below:

| Call ID (sum) | udo\_typename | udo\_subtypename                                      | Percentage |
| ------------- | ------------- | ----------------------------------------------------- | ---------- |
| 2209538       | Claim         | General Status                                        | 86.169%    |
| 112341        | Claim         | Document Verification                                 | 4.381%     |
| 111377        | Claim         | ITF/Generate ITF                                      | 4.344%     |
| 107850        | Claim         | Exam                                                  | 4.206%     |
| 5320          | Claim         | DIC (Dependency and Indemnity Compensation) / Accrued | 0.207%     |
| 3920          | Claim         | Withdraw a Claim/Contention                           | 0.153%     |
| 3722          | Claim         | ITF/ VA Form 21-0966                                  | 0.145%     |
| 2403          | Claim         | Death Pension / A and A / Housebound                  | 0.094%     |
| 2137          | Claim         | Burial Plot and Transportation benefits               | 0.083%     |
| 1734          | Claim         | Reconsideration Request                               | 0.068%     |
| 1708          | Claim         | MOD Payments                                          | 0.067%     |
| 1409          | Claim         | Income Adjustment                                     | 0.055%     |
| 712           | Claim         | IVM                                                   | 0.028%     |
| 8             | Claim         | General Inquiry                                       | 0.000%     |
| 4             | Claim         | Request for Benefit Letter                            | 0.000%     |
| 4             | Claim         | Request for Forms                                     | 0.000%     |
| 4             | Claim         |                                                       | 0.000%     |
| 2             | Claim         | Email Blank Forms                                     | 0.000%     |
| 2             | Claim         | Supplemental Claim Update                             | 0.000%     |
| 1             | Claim         | Add School Aged Children                              | 0.000%     |
| 1             | Claim         | Remote Proofing                                       | 0.000%     |
| 1             | Claim         | Explanation of Letter                                 | 0.000%     |
| 1             | Claim         | Withdraw Issue                                        | 0.000%     |
