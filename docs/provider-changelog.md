# Provider changelog

## 2026-05-02

For new card payment flows, move from the legacy Charges create path to PaymentIntents.

- Affected endpoint: POST /v1/charges
- Replacement endpoint: POST /v1/payment_intents
- Deprecation date: 2026-11-30

## 2026-05-01

Charges remain available for legacy card payments.
