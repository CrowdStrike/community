---
title: Open Source Policy
description: This is a documentation page.
permalink: /open-source-policy/

layout: post
sidenav: open-source-policy
subnav:
  - text: CrowdStrike Engineering
    href: '#crowdstrike-engineering'
  - text: Everyone Else
    href: '#everyone-else'
---

## CrowdStrike Engineering

Members of CrowdStrike's Engineering organization should follow the engineering-specific open source process and contribution guidance as documented on the internal engineering wiki.


## Everyone Else
### Project Licensing
* **Use the most permissive license possible with a bias towards community building**.

  * This will often be [The Unlicense](https://opensource.org/licenses/unlicense), or if copyright should be retained, [The MIT License](https://opensource.org/licenses/MIT) is popular.

  * If your project is content focused, such as training materials and coursebooks, consider one of the licenses from [Creative Commons](https://creativecommons.org/choose/).

* Regardless of license choice, **your LICENSE file should contain language explicitly stating the project content is provided "as is" without warranty**. Both The Unlicense and MIT License contain this language.

* Somewhere in your repository, most likely in the README file, should be an **explicit statement
stating your initiative is a *project* and not *product*\**. Set expectations upfront and guide the community to your projects collaboration spaces. For example, on the [FalconPy SDK Project](https://github.com/CrowdStrike/falconpy), the following language was used:

<table>
<td>
<code>
# Support & Community Forums
<p>FalconPy is an open source project, not a formal CrowdStrike product, to assist developers implement CrowdStrike's APIs within their applications. As such it carries no formal support, express or implied.</p>

<p>:fire: Is something going wrong? :fire:<br/>
GitHub Issues are used to report bugs. Submit a ticket here:<br/>
[https://github.com/CrowdStrike/falconpy/issues/new/choose](https://github.com/CrowdStrike/falconpy/issues/new/choose)</p>

<p>GitHub Discussions provide the community with means to communicate. There are four discussion categories:<br/>
  * :speech_balloon: [**General**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AGeneral) : Catch all for general discussions. <br/>
  * :bulb: [**Ideas**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AIdeas): Have a suggestion for a feature request? Is there something the community or project could improve upon? Let us know here.<br/>
  * :pray: [**Q&A**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AQ%26A): Have a question about how to accomplish something? A usability question? Submit them here!<br/>
  * :raised_hands: [**Show and Tell**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3A%22Show+and+tell%22): Share with the community what you're up to! Perhaps this is letting everyone know about your upcoming conference talk, share a project that has embedded FalconPy, or your recent blog.</p>
  </code>
  </td>
</table>

* Individual files in your project do not need licensing incorporated into the top of the file. **Use a whole-of-project LICENSE file.**


### Upstream Participation
**No special permission is needed to contribute to upstream projects or communities**. 

Do not release code into open source projects that incorporates CrowdStrike proprietary information. Speak with your team lead or manager, and if further assistance is needed, refer to Shawn Wells, Vice President of Solution Architecture, at [shawn.wells@crowdstrike.com](mailto:shawn.wells@crowdstrike.com).


### Joining the CrowdStrike GitHub Organization
* [Open a ticket in this repo](https://github.com/CrowdStrike/Open-Source-Policy/issues) outlining who you are (name, @crowdstrike.com EMail). Someone will reach out to you on the internal slack to verify and create your account.

* Should you not receive a response in 1-2 business days, ping `#open-source-contributors` on internal Slack.

* Accounts associated with CrowdStrike's corporate GitHub organization require [Two-factor Authentication (2FA)](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/securing-your-account-with-two-factor-authentication-2fa) to be enabled.

* GitHub accounts do <b><u>not</u></b> need to be associated with your CrowdStrike EMail address. Your contributions should carry on with you!
