BOUNDARY OPERATOR FORMALIZATION

VERSION 0.1

====================================================================

ABSTRACT

This document defines the Boundary Operator for
Boundary-Horizon Logic (BHL).

Earlier formulations of the Boundary-Horizon-Finitude (BHF)
Framework identified the horizon with the residual difference
between an outer and inner domain.

H(Ωout, Ωin) = Ωout − Ωin

While useful intuitively, this interpretation treats the
horizon as a region.

Boundary-Horizon Logic instead interprets a horizon as a
boundary object: the interface at which propositional
classifications change between informational domains.

This separates:

- Boundary
- Horizon
- Distinction Region

into distinct mathematical concepts.

====================================================================

1. BOUNDARY SYSTEMS

Let

(B, ≤)

be a partially ordered set of informational domains
called boundaries.

For boundaries

Ωa, Ωb ∈ B

the relation

Ωa ≤ Ωb

means that Ωa is informationally contained within Ωb.

====================================================================

2. PROPOSITION SPACE

Let

P

denote the set of propositions.

Each proposition is evaluated relative to a boundary.

Define the localization function

LocΩ

such that

LocΩ : P → {X, U, H, KT, KF}

where

X  = External
U  = Unknown
H  = Horizon
KT = Known True
KF = Known False

The localization map assigns a unique informational
state to each proposition relative to a boundary.

====================================================================

3. BOUNDARY OPERATOR

DEFINITION

The Boundary Operator is the function

∂ : B × B → H

defined whenever

Ωin ≤ Ωout

For two boundaries,

∂(Ωout, Ωin)

is the collection of propositions whose classifications
differ between the two domains.

Formally:

∂(Ωout, Ωin)

=

{ p ∈ P :

  LocΩout(p) ≠ LocΩin(p)

}

====================================================================

4. INTERPRETATION

The boundary consists precisely of those propositions
that change state when crossing from one informational
domain to another.

Thus:

- Boundaries are informational domains.
- Horizons are boundary interfaces.
- Distinction arises from state transitions.
- Classification change generates boundary structure.

A proposition belongs to a horizon precisely when its
classification differs between two boundaries.

====================================================================

5. EXAMPLE

Assume

Ω1 < Ω2

Suppose proposition p satisfies

LocΩ1(p) = U

and

LocΩ2(p) = H

Then

p ∈ ∂(Ω2, Ω1)

The proposition lies on the horizon separating the two
informational domains.

====================================================================

6. FUNDAMENTAL PROPERTIES

PROPERTY B1: REFLEXIVITY

∂(Ω, Ω) = ∅

PROOF

For every proposition p:

LocΩ(p) = LocΩ(p)

No proposition changes classification relative to
the same boundary.

Therefore

∂(Ω, Ω) = ∅

QED.

--------------------------------------------------------------------

PROPERTY B2: BOUNDARY MEMBERSHIP

For every proposition p:

p ∈ ∂(Ωa, Ωb)

if and only if

LocΩa(p) ≠ LocΩb(p)

PROOF

Immediate from the definition of the Boundary Operator.

QED.

--------------------------------------------------------------------

PROPERTY B3: BOUNDARY MONOTONICITY

If

Ωa ≤ Ωb ≤ Ωc

then

∂(Ωa, Ωc)

⊆

∂(Ωa, Ωb)

∪

∂(Ωb, Ωc)

INTERPRETATION

Every classification change observed across a larger
boundary transition must occur either in one of the
intermediate transitions or in their union.

====================================================================

7. DISTINCTION REGION

The Boundary Operator must not be confused with the
Distinction Region.

Define

D(Ωout, Ωin)

=

Ωout \ Ωin

The distinction region measures informational
separation.

The boundary operator identifies the horizon at which
classifications change.

Therefore:

Boundary ≠ Difference

and generally

∂(Ωout, Ωin)

≠

D(Ωout, Ωin)

====================================================================

8. UNIVERSAL HORIZON

Let

UH

denote the maximal boundary.

Define

UH = sup(B)

Alternatively the global horizon structure may be
represented by

HU

=

⋃ ∂(Ωi, Ωj)

taken over all boundaries Ωi and Ωj in B.

This construction captures all distinguishable
classification transitions across every boundary system.

====================================================================

9. CONCEPTUAL CONSEQUENCES

This definition changes the interpretation of the
framework.

Older formulations treated the horizon as a residual
region:

Ωout − Ωin

The Boundary Operator instead treats the horizon as a
transition interface:

∂(Ωout, Ωin)

The key principle is:

A horizon is not what remains after a boundary is removed.

A horizon is where classification changes.

This interpretation aligns naturally with logic,
information theory, state-transition systems,
and epistemic reasoning.

====================================================================

SUMMARY

The Boundary Operator is defined by

∂(Ωout, Ωin)

=

{ p :

  LocΩout(p) ≠ LocΩin(p)

}

Under this formulation:

- Boundaries are informational domains.
- Horizons are transition interfaces.
- Distinction regions measure separation.
- Proposition state changes generate boundary structure.

The operator provides the formal mechanism through
which informational horizons emerge within
Boundary-Horizon Logic.

====================================================================

END OF DOCUMENT
