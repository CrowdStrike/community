---
title: Contributing to a Project
description: Guidance for Contributing to CrowdStrike Open Source Projects
permalink: /contributing/

layout: post
sidenav: contributing
subnav:
  - text: Welcome
    href: '#welcome'
  - text: How do I make a contribution?
    href: '#how-do-i-make-a-contribution'
  - text: Where can I go for help?
    href: '#where-can-i-go-for-help'
  - text: What does the Code of Conduct mean for me?
    href: '#what-does-the-code-of-conduct-mean-for-me'
---

# Welcome!
Welcome and thank you for your interest in contributing to a CrowdStrike project! We recognize contributing to a project is no small feat! The guidance here aspires to help onboard new community members into how CrowdStrike-led projects tend to operate, and by extension, make the contribution process easier.

# How do I make a contribution?
Never made an open source contribution before? Wondering how contributions work in CrowdStrike projects? Here is a quick rundown!

1. Find an issue that you are interested in addressing, or a feature you would like to add. These are often documented in the project repositories themselves, frequently in the `issues` section.

2. Fork the repository associated with project to your GitHub account. This means that you will have a copy of the repository under *your-GitHub-username/repository-name*. 

   Guidance on how to fork a repository can be found at [https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository).

3. Clone the repository to your local machine using ``git clone https://github.com/github-username/repository-name.git``.

    GitHub provides documentation on this process, including screenshots, here:
[https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#about-cloning-a-repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#about-cloning-a-repository)

4. Create a new branch for your changes. This ensures your modifications can be uniquely identified and can help prevent rebasing and history problems. A local development branch can be created by running a command similar to:

    ``git checkout -b BRANCH-NAME-HERE``

5. Make the appropriate changes for the issue you are trying to address or the feature you'd like to add.

6. Add the file contents of the changed files to the "snapshot" git uses to manage the state of the project (also known as the index). Here's the git command that will add your changes:

    ``git add insert-paths-of-changed-files-here``

7. Use `git commit` to store the contents of the index with a descriptive message. This message should outline what was changed. For example:

    ``git commit -m "Added Dockerfile for Ubuntu-based deployments"``

8. Push your local changes back to gihub.com:

    ``git push origin BRANCH-NAME-HERE``

9. Submit a pull request to the upstream project. Documentation on this process, including screen shots, can be found here:

[https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork)

10. Once submitted, a maintainer will review your pull request. They may ask for additional changes, or clarification, so keep an eye out for communication! GitHub automatically sends an email to your email address whenever someone comments on your pull request.

11. Celebrate your contribution after your pull request is merged! All changes move the project forward, and we thank you for helping the community!

## Rebase Early, Rebase Often!
Projects tend to move at a fast pace, which means your fork may become behind upstream. Keeping your local fork in sync with upstream is called `rebasing`. This ensures your local copy is frequently refreshed with the latest changes from the community. 

Frequenty rebasing is *strongly* encouraged. If your local copy falls to far behind, you may encounter merge conflicts when submitting pull request. If this happens, you'll have to triage (often by hand!) the differents in your local repository versus the changes upstream.

* Documentation on how to sync/rebase your fork can be found here:
[https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)

* For handling merge conflicts, refer to:
[https://opensource.com/article/20/4/git-merge-conflict](https://opensource.com/article/20/4/git-merge-conflict)


# Where can I go for help?
## Submitting a Ticket
General questions relating a project should be opened in that projects repository. Examples would be troubleshooting errors, submitting bug reports, or asking a general question/request for clarification.

If your question is of the broader CrowdStrike community, please [open a community discussion](https://github.com/CrowdStrike/community/discussions/new).

## Submitting a New Project Idea
 If you do not see a project, repository, or would like the community to consider working on a specific piece of technology, please [open a community ticket](https://github.com/CrowdStrike/community/issues/new). 


# What does the Code of Conduct mean for me?
Our Code of Conduct means that you are responsible for treating everyone on the project with respect and courtesy regardless of their identity. If you are the victim of any inappropriate behavior or comments as described in our Code of Conduct, we are here for you and will do the best to ensure that the abuser is reprimanded appropriately, per our code.

Each CrowdStrike project should have its own group of maintainers that issues can be raised to. These individuals are accountable for enforcing the CrowdStrike Code of Conduct within the project.

## Escalation Path
If you do not feel safe communicating with the project maintainers, or if you feel the situation warrants, please escalate to:

Shawn Wells<br/>
Global Vice President, Solution Architecture<br/>
[shawn.wells@crowdstrike.com](shawn.wells@crowdstrike.com)<br/>
Personal Cell: [+1 443 534 0130](tel:+14435340130) (U.S. Eastern, GMT-5)
