#################
Configuration DSL
#################

A small DSL is bein used to set up the grammar.

Files using this DSL are read and processed, and the data is then sent to the
grammar factory to build the grammar.

An example of this DSL, defining the Agreement Record:

.. code-block::

    transaction_record:
        id: agreement
        head: AGR
        rules:
          [
          sequence
            [
            field: submitter_agreement_n
            field: international_standard_code
            field: agreement_type
            field: agreement_start_date
            field: agreement_end_date
            field: retention_end_date
            field: prior_royalty_status
            field: prior_royalty_start_date
            field: post_term_collection_status
            field: post_term_collection_end_date
            field: date_of_signature
            field: number_of_works
            field: sales_manufacture_clause
            field: shares_change
            field: advance_given
            field: society_assigned_agreement_n
            ]
        ]

*****************
Rules composition
*****************

Rules are composed of several smaller rules. The terminal rules are the fields,
defined on their own module.

This creates a tree of rules.

There are two groups of rules in a tree:

- Rules. Composed from a series of other rules.
- Rules lists. These are a set of rules, grouped by a combinatory rule.

Note that rules can be terminal rules. All rule blocks should generate trees
ending in terminal rules.

Rules tree
==========

Show how the rules are defined as a tree.

*********
Structure
*********

The DSL consists on a series of blocks, each of them representing a grammar rule.

These rules represent a logical section of the file, and may be for a line, or
for a series of them.

They have the following structure, which only shows compulsory fields:

.. code-block::

    rule_group_1:
        id: rule_id_1
        rules:
          [
          internal_rules_list
            [
            rule_group_2: rule_id_2
            rule_group_1: rule_id_3
            rule_group_2: rule_id_4
            ]
          rule_group_2: rule_id_5
        ]

Compulsory fields
=================

Each block has a set of required fields:

===============  ==============================================
Field            Notes
===============  ==============================================
Root rule group  The root of the block. In the example it is 'transaction_record'. It indicates the global group to which it belongs.
Rule id          Identifier for this rule
Rules            The smaller rules which compose this rule
Internal rules   A new tree of rules
Rule group       A group of rules
===============  ==============================================
