# Acme

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [General](#general)
- [Development environment](#development-environment)
- [Comments](#comments)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## General

Trivial implementation of Sales System. Consists of:

 - `Product` - basic product entity.
 - `ProductCatalogue` - stores `Product`s as dict where key is the `Product` code.
 - `DeliveryChargeRule` - defines single rule to calculate delivery cost.
 - `SpecialOffer` - defines single rule to calculate special offer discount.
 - `Basket` - takes `ProductCatalogue`, list of `DeliveryChargeRule`s and optional list of `SpecialOffer`s as parameters.
    Possible to add products by `add()` method and get total cost by `total()` method
    (takes into account the delivery rules and special offers).

Predefined lists of `DeliveryChargeRule`s and `SpecialOffer`s are populated by decorating particular rules and offers.

## Development environment

Run environment is Python 3.9.

Requirements are described in `requirements.txt`.

Create virtual environment, activate it and install requirements.

To run all tests run: `python -m pytest`.

It is highly recommended tu use [pre commit](https://pre-commit.com). The pre-commits
installed via pre-commit tool handle automatically linting (including automated fixes) as well,
so you do not have to run it yourself.

Example commands to run locally:

```shell
git clone https://github.com/TobKed/acme.git
cd acme

python3.9 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python -m pytest
```

## Comments

 1. Projects is very simple. I avoided over-engineering for sake of simplicity and limited time I wanted to spend on it.
 1. `ProductCatalogue` is very simple product database.
    It could be moved to abstract class which defines `get_product()` method as interface only.
    Then particular product catalogues could store products in other way than simple dictionary
    (csv, sql, external service etc.).
    With common interface product catalogues could be easily interchangeable.
 1. For `DeliveryChargeRule` and `SpecialOffer` I used kind if strategy pattern
    (inspired by "Fluent Python" book which I am reading currently).
    `Basket` uses `__get_delivery_cost()`, `__get_best_special_offer_discount()` methods to choose which strategy apply.
    Particular offers are functions based and described by typing alias but during further development
    they could be potentially described as abstract class
    (then `__get_delivery_cost()`, `__get_best_special_offer_discount()` could be moved to relevant classes).
 1. Docker image could be created alongside with Makefile to easily run tests and other commands.
