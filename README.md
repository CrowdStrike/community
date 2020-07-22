# CrowdStrike's Open Source Policy &amp; Contribution Guide

In development. EVERYTHING HERE IS CURRENTLY DRAFT! Pull requests appreciated and welcome as we further develop our open source usage and contribution guidelines. 

The purpose of this policy is to outline the process for CrowdStrike personnel to release open source code. This policy applies to all types of projects (i) that relate to CrowdStrike's business or CrowdStrike's actual or demonstratably anticipated research and development, (ii) written on CrowdStrike time, and/or (iii) written using CrowdStrike resources.

- [CrowdStrike's Open Source Policy &amp; Contribution Guide](#crowdstrike-s-open-source-policy--amp--contribution-guide)
  * [Joining the CrowdStrike GitHub Org](#joining-the-crowdstrike-github-org)
  * [Creating Open Source Projects](#creating-open-source-projects)
    + [Initiating CrowdStrike Projects](#initiating-crowdstrike-projects)
    + [Contributing to a Third Party (community) Projects](#contributing-to-a-third-party--community--projects)
    + [Open Sourcing Previously Internal-Only Projects](#open-sourcing-previously-internal-only-projects)
    + [Personal Participation in Open Source](#personal-participation-in-open-source)
  * [Consumption of Open Source](#consumption-of-open-source)
    + [Process](#process)
    + [Compliance](#compliance)
    + [Ongoing Verification](#ongoing-verification)
  * [Open Source Licenses](#open-source-licenses)
      - [Acceptable Licenses](#acceptable-licenses)
  * [GitHub Account Guidelines](#github-account-guidelines)
    + [Account Settings](#account-settings)
    

## Joining the CrowdStrike GitHub Org
[Open a ticket in this repo](https://github.com/CrowdStrike/Open-Source-Policy/issues) outlining who you are (name, @crowdstrike.com EMail). Someone will reach out to you on the internal slack to verify and create your account.

Should you not receive a response in 1-2 days, ping ``#github-management`` on internal Slack.

## Creating Open Source Projects
Anything that risks CrowdStrike's competitive advantage should not be released as open source. Any code released as open source should be generally useful, such as fix bugs in an open source project, rather than a CrowdStrike-specific application. In addition, no code may be released as open source that incorporates CrowdStrike proprietary information.

### Initiating CrowdStrike Projects
Guidance on initiating "official" CrowdStrike projects, under the CrowdStrike GitHub Org, is TBD.

### Contributing to a Third Party (community) Projects
Guidance on official participation in broader community projects (eg as part of your day job) is TBD

### Open Sourcing Previously Internal-Only Projects
**1. Approval**

After you have confirmed that your proposed contribution is within the scope of permitted release as outlined in this policy, please send an EMail outlining the details of the contribution for approval to your manager or someone in your management chain who holds a Director title or above.

**2. Visiblilty**

Once manager approval has both been provided via EMail, send the proposal description and the names of the approvers to CrowdStrike Engineering's open source team.

**3. Release**

  - All code must be approved by a Principal Engineer (if you fall within the Engineering org) or a Senior Solution Architect (if you reside within the Solution Architecture org).
  - Add the details of the release and applicable approvals in the CrowdStrike internal wiki. Legal/Finance will have access to this for intellectual property due dilligence reasons.
  - Once all the steps above have been completed, the code may be released as approved.
 
**4. Updates**

 Future updates to code released through this process do not need to be resubmitted for approval outlined in step 1. Instead, such updates only require steps 2-3 to be completed prior to release.
 
 For questions about open sourcing internal technology, please contact David Foley in Legal: [david.foley@crowdstrike.com](mailto:david.foley@crowdstrike.com).

### Personal Participation in Open Source
Guidance on personal projects will go here.

## Consumption of Open Source
CrowdStrike employees and contractors may only use open source software in connection with the development, support, or provision of CrowdStrike offerings in compliance with this policy.

### Process

**1. Approval**
* To request approval for the usage of a particular open source software package, create anew row on the OSS Usage page on the internal wiki following the current template. You must fill in the following information for the specific portion of our code this open source software will be used in:
   * Name and version of the open source software package
   * The dates of such usage and when the open source software was retrieved
   * URL of the open source software package/project web page
   * The type of license; if multiple licenses are used for a project, then each license needs to be liste
   * Whether the open source sofreware is (or will be) modified or unmodified
   * How the open source software is implemented in the CrowdStrike offering (e.g., standalone binary, dynamic/static linking, Imported (dynamic languages), etc.)

* Once the listing has been added, please send an email for approval referencing such listing along with a description of how it is used and why we need the open source software to the following:
    * Someone in your management chain who holds a Director title or above and/or a Principle Engineer
    * [legal@crowdstrike.com](mailto:legal@crowdstrike.com), as follows:
      * If the OSS will be part of any offering distributed to a third-party company, include [legal@crowdstrike.com](mailto:legal@crowdstrike.com)
      * If the OSS will be part of an offering that is hosted only, but the license is not listed as "Approved" under the [Acceptable Licenses](#Acceptable-Licenses) matrix below, include [legal@crowdstrike.com](mailto:legal@crowdstrike.com)
      * If the OSS will be part of an offering that is hosted only and the license is listed as "Approved" under the [Acceptable Licenses](#Acceptable-Licenses) matrix below, no further legal approvals are necessary and the requester may put "Legal Pre-Approved" in the "Legal Approved" column.

**2. Visibility**
Once manager and legal approvals have both been provided via email, send a notification of the update to CrowdStrike's open source team. This alias is for awareness and will have members from legal and engineering.

**3. Tracking**
* Once OSS has been approved for a particular use case, the OSS package may be used as approved. The request for approval and subsequent approvals should be left on the OSS disclosure page on the Wiki for tracking purposes.
* If the OSS usage is not approved, the proposed approval request should be removed from the OSS disclosure page on the wiki.

### Compliance
Most OSS licenses require some degree of informational compliance when distributing (e.g. providing attribution, copies of licenses or source code, or identifying modified files). Affirmative efforts must be made to ensure compliance requirements are met even when OSS with an "Approved" license is used. Please develop an appropriate compliance plan and consult with CrowdStrike legal if you are unsure of the compliance obligations for any open source software.

### Ongoing Verification
Automated WhiteSource scans performed by CrowdStrike shall be reviewed periodically to verify compliance and tracking of open source software.


## Open Source Licenses
#### Acceptable Licenses
The following chart identifies licenses which are pre-approved by CrowdStrike legal and those that require additional review.

| License | Hosted only, not delivered | Distributed - unmodified | Distributed - modified |
|:--------|:--------------------------:|:------------------------:|:----------------------:|
| BSD | Approved | Approved | Approved |
| MIT | Approved | Approved | Approved |
| ZLIB | Approved | Approved | Approved |
| ISC | Approved | Approved | Approved |
| Apache | Approved | Approved | Approved |
| Mozilla | Approved | Approved | *Requires Approval* |
| Eclipse | Approved | Approved | *Requires Approval* |
| CDDL | Approved | Approved | *Requires Approval* |
| LGPL v2.1 | Approved | *Requires Approval* | *Requires Approval* |
| GPL v2 | *Requires Approval* | *Requires Approval* | *Requires Approval* |
| GPL / LGPL v3 | *Requires Approval* | *Requires Approval* | **Prohibited** |
| "Affero" Licenses (AGPL) | **Prohibited** | **Prohibited** | **Prohibited** |
| [OSL](https://opensource.org/licenses/OSL-3.0) | **Prohibited** | **Prohibited** | **Prohibited** |
| [EUPL](https://joinup.ec.europa.eu/collection/eupl/eupl-text-11-12) | **Prohibited** | **Prohibited** | **Prohibited** |
| [CPAL](https://opensource.org/licenses/CPAL-1.0) | **Prohibited** | **Prohibited** | **Prohibited** |
| [Sleepycat](https://opensource.org/licenses/Sleepycat) | **Prohibited** | **Prohibited** | **Prohibited** |

Any other license not listed above requires approval by [legal@crowdstrike.com](mailto:legal@crowdstrike.com).

A list of licenses being reviewed:

| License | Description |
| ------- | ----------- |
| [Creative Commons Zero (CCO)](https://creativecommons.org/publicdomain/zero/1.0/) | Public domain dedication, recommended as a way to disclaim copyright to the maximum extent possible. |
| [Unlicense](https://unlicense.org/) | Free and unencumbered software released into the public domain. At CrowdStrike this is often used for scripts and automation snippets (eg CloudFormation templates). |
| GNU LGPL | |
| Apache 2.0 | |
| BSD 2-Clause License | |
| BSD 3-Clause License | |



## GitHub Account Guidelines

### Account Settings
* Enable MFA
