.. currentmodule:: ncjishaku

What's new?
================

Version 3.1.0b2
---------------

This version incorporates upstream updates.
The original update information is as follows:

This version is a feature & patch release, being expedited due to Discord introducing strange behaviour regarding code blocks.

The changes in this release are:

- The ``jsk rerun`` command, which allows a previously sent jishaku command to be executed again without needing to re-upload attachments or other message details (PR `#251 <https://github.com/scarletcafe/jishaku/pull/251>`_, thanks `@WitherredAway <https://github.com/WitherredAway>`_ for implementation).
- Any command that uses code block converters will now strip formatter characters silently added by certain Discord clients in presently-unknown circumstances. This prevents the inability to use a large portion of jishaku in these situations (issue `#253 <https://github.com/scarletcafe/jishaku/issues/253>`_, thanks `@Stacer-Varien <https://github.com/Stacer-Varien>`_ and `@Captain8771 <https://github.com/Captain8771>`_ for reporting).

Version 3.0.0rc1
----------------

This release is the first version of ncjishaku, which was forked from `jishaku <https://github.com/scarletcafe/jishaku>`_ and ported to nextcord v3.

Most features should work the same as the original jishaku, but YouTube-related features have been removed in accordance with Discord's Terms of Service.
