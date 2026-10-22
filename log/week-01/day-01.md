# Day 1 · Securing my AWS account

**Did:** Turned on MFA for root, created an admin group, created Semiat-admin with MFA (passkey).

**Why:** Root has unlimited power and can't be restricted, so it stays locked away. Daily work happens as an IAM user.

**Learned:** Authentication ≠ authorization. I could sign in as Semiat-admin but got "not authorized" until the group had AdministratorAccess.

**Parked:** Budgets errors even on root. Revisit before upgrading in February.
