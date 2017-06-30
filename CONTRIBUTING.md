# Contributing to Vent Plugins

Want to hack on Vent plugins? Awesome! Here are instructions to get you
started.  They are probably not perfect, please let us know if anything
feels wrong or incomplete.

Looking for Vent? [You'll find it here.](https://github.com/CyberReboot/vent)

## Contribution guidelines

### Pull requests are always welcome

We are always thrilled to receive pull requests, and do our best to
process them as fast as possible. Not sure if that typo is worth a pull
request? Do it! We will appreciate it.

If your pull request is not accepted on the first try, don't be
discouraged! If there's a problem with the implementation, hopefully
you received feedback on what to improve.

We're trying very hard to keep Vent lean and focused. We don't want it
to do everything for everybody. This means that we might decide against
incorporating a new feature. However, there might be a way to implement
that feature *on top of* Vent Plugins!

### Create issues...

Any significant improvement should be documented as [a github
issue](https://github.com/CyberReboot/vent-plugins/issues) before anybody
starts working on it.

### ...but check for existing issues first!

Please take a moment to check that an issue doesn't already exist
documenting your bug report or improvement proposal. If it does, it
never hurts to add a quick "+1" or "I have this problem too". This will
help prioritize the most common problems and requests.

### Conventions

Fork the repo and make changes on your fork in the master branch. (Vent loads
plugins from the Master branch exclusively, so it won't pickup changes made in
a feature branch!)

Make sure you include relevant updates or additions to documentation and
tests when creating or modifying features.

Pull request descriptions should be as clear as possible and include a
reference to all the issues that they address.

Code review comments may be added to your pull request. Discuss, then make the
suggested modifications and push additional commits to your feature branch. Be
sure to post a comment after pushing. The new commits will show up in the pull
request automatically, but the reviewers will not be notified unless you
comment.

Commits that fix or close an issue should include a reference like
`Closes #XXX` or `Fixes #XXX`, which will automatically close the issue
when merged.

Add your name to the AUTHORS file, but make sure the list is sorted and
your name and email address match your git configuration. The AUTHORS
file is regenerated occasionally from the git commit history, so a
mismatch may result in your changes being overwritten.

## Decision process

### How are decisions made?

Short answer: with pull requests to the Vent plugins repository.

All decisions affecting Vent plugins, big and small, follow the same 3 steps:

* Step 1: Open a pull request. Anyone can do this.

* Step 2: Discuss the pull request. Anyone can do this.

* Step 3: Accept or refuse a pull request. A maintainer does this.

### How can I become a maintainer?

* Step 1: Learn the code inside out
* Step 2: Make yourself useful by contributing code, bugfixes, support etc.

Don't forget: being a maintainer is a time investment. Make sure you will
have time to make yourself available.  You don't have to be a maintainer
to make a difference on the project!

### What are a maintainer's responsibility?

It is every maintainer's responsibility to:

* 1) Deliver prompt feedback and decisions on pull requests.
* 2) Be available to anyone with questions, bug reports, criticism etc. on Vent.

### How is this process changed?

Just like everything else: by making a pull request :)

*Derivative work from [Docker](https://github.com/docker/docker/blob/master/CONTRIBUTING.md).*