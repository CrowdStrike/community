# CrowdStrike's Open Source Policy &amp; Contribution Guide

In development. EVERYTHING HERE IS CURRENTLY DRAFT! Pull requests appreciated and welcome as we further develop our open source usage and contribution guidelines. 


## Joining the CrowdStrike GitHub Org
[Open a ticket in this repo](https://github.com/CrowdStrike/Open-Source-Policy/issues) outlining who you are (name, @crowdstrike.com EMail). Someone will reach out to you on the internal slack to verify and create your account.

Should you not receive a response in 1-2 days, ping ``#github-management`` on internal Slack.

## Creating Open Source Projects
### Initiating CrowdStrike Projects
Guidance on initiating "official" CrowdStrike projects, under the CrowdStrike GitHub Org, is TBD.

### Contributing to a Third Party (community) Projects
Guidance on official participation in broader community projects (eg as part of your day job) is TBD

### Personal Participation in Open Source
Guidance on personal projects will go here.

## Open Source Licenses
#### Acceptable Licenses
The following licenses are acceptable for use:

| License | Description |
| ------- | ----------- |
| [Creative Commons Zero (CCO)](https://creativecommons.org/publicdomain/zero/1.0/) | Public domain dedication, recommended as a way to disclaim copyright to the maximum extent possible. |
| [Unlicense](https://unlicense.org/) | Free and unencumbered software released into the public domain. At CrowdStrike this is often used for scripts and automation snippets (eg CloudFormation templates). |

For future consideration:
* MIT License
* GNU LGPL
* Apache 2.0
* BSD 2-Clause License
* BSD 3-Clause License
* ISC License

#### Unacceptable Licenses

Legal approval is required before initiating a project with the following licenses, embedding a technology with any of these licenses into a CrowdStrike product, or contributing to a 3rd party project which uses a license listed below:

| License | Rationale |
| ------- | --------- |
| [GNU GPL](https://choosealicense.com/licenses/gpl-3.0/) (version 1, [version 2](http://www.gnu.org/licenses/gpl-2.0.txt), [version 3](http://www.gnu.org/licenses/gpl-3.0.txt), or any future versions) | GPL-licensed technologies cannot be linked to from non-GPL projects. |
| [GNU AGPLv3]() | AGPL-licensed technologies cannot be linked to from non-GPL projects. |
| [Open Software License (OSL)](https://opensource.org/licenses/OSL-3.0) | Copyleft license. In addition, the FSF [recommends against its use](https://www.gnu.org/licenses/license-list.en.html#OSL). |



## GitHub Account Guidelines

### Account Settings

| Permission  | MFA Enabled |
|-------------|:--:|
| CrowdStrike GitHub Org Admin  | Y  |
| ``merge`` access to CrowdStrike project  | Y  |
