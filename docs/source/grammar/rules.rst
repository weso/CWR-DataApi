#####
Rules
#####

Depending on their scope, there are three kinds of rules:

- Terminal rules. These are fields, and are not composed by other rules.
- Record. These are the lines from the CWR files, and are composed of terminal rules.
- Group. These are aggregations of records. They may be composed of of any combination of rules, including other groups.

In practice, only terminal rules are different.

*****************
Rules aggregation
*****************

While it may seem that only groups are a complex aggregation of rules, actually
the records are not much different, as they aggregat

**********
Rules tree
**********

While at first it may seem that only the rules groups, being the most complex,
take the shape of a tree. Actually all, except for terminal rules, are trees of
rules.

