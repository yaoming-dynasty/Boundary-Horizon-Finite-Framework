Boundary-Horizon Logic (BHL) Lattice Structure
Abstract

Boundary-Horizon Logic (BHL) extends the Boundary-Horizon-Finitude (BHF) framework by introducing a formal truth space based on informational boundaries and distinguishability. Rather than treating propositions as merely true or false, BHL classifies propositions according to their position relative to an observer's informational boundary.

This document introduces the BHL truth-state algebra and demonstrates that, with the introduction of a Universal Horizon element, the resulting structure forms a bounded lattice.

1. Motivation

Classical logic assumes every proposition is either true or false.

Many important statements resist immediate classification:

Russell's Paradox
The Liar Paradox
Gödel Self-Reference
Unresolved Mathematical Conjectures
Incomplete Scientific Knowledge

BHL proposes that before truth can be evaluated, a proposition must first be located relative to an informational boundary.

2. Truth States

Define the truth space:

T={X,U,H,KT,KF}\mathbb{T} = \{X,U,H,KT,KF\}T={X,U,H,KT,KF}

where:

Symbol	MeaningX	External to current domain
U	Unknown but within domain
H	Horizon state (distinguishable but unresolved)
KT	Known True
KF	Known False
3. Ordering Principle

The ordering is based on distinguishability.

X<U<H<KTX < U < H < KTX<U<H<KT

and

X<U<H<KFX < U < H < KFX<U<H<KF

Visualized:

Plain Text
KT KF
\ /
H
|
U
|
X
 

Interpretation:

X contains no distinguishable information.
U contains inaccessible information.
H contains distinguishable but unresolved information.
KT and KF contain resolved information.
4. Failure of Lattice Closure

A lattice requires every pair of elements to possess:

A unique meet (greatest lower bound)
A unique join (least upper bound)

Consider:

Plain Text
KT and KF

Their greatest lower bound is:

Plain Text
H

However no least upper bound exists.

Therefore:

KT∨KFKT \vee KFKT∨KF

is undefined.

Consequently:

(T,≤)(\mathbb T,\le)(T,≤)

is not a lattice.

5. Universal Horizon

Introduce a sixth element:

UHUHUH

called the Universal Horizon.

The Universal Horizon represents the horizon containing every possible boundary system.

Formally:

∀Ωi,Ωi≺UH\forall \Omega_i, \quad \Omega_i \prec UH∀Ωi​,Ωi​≺UH

Every informational boundary exists within the Universal Horizon.

6. Extended Ordering

Adding the Universal Horizon yields:

Plain Text
UH
/ \
KT KF
\ /
H
|
U
|
X

with ordering:

X<U<H<KT<UHX<U<H<KT<UHX<U<H<KT<UH

and

X<U<H<KF<UH.X<U<H<KF<UH.X<U<H<KF<UH.
7. Meet and Join Operations
Meet

The meet operator represents shared certainty.

a∧ba \wedge ba∧b

Examples:

KT∧KF=HKT \wedge KF = HKT∧KF=H KT∧U=UKT \wedge U = UKT∧U=U KT∧KT=KTKT \wedge KT = KTKT∧KT=KT
Join

The join operator represents the least common resolution space.

a∨ba \vee ba∨b

Examples:

KT∨H=KTKT \vee H = KTKT∨H=KT U∨H=HU \vee H = HU∨H=H KT∨KF=UHKT \vee KF = UHKT∨KF=UH
8. The BHL Lattice Theorem
Theorem

Let

L={X,U,H,KT,KF,UH}L = \{X,U,H,KT,KF,UH\}L={X,U,H,KT,KF,UH}

with ordering:

X<U<H<KT<UHX<U<H<KT<UHX<U<H<KT<UH

and

X<U<H<KF<UH.X<U<H<KF<UH.X<U<H<KF<UH.

Then every pair of elements possesses:

a unique greatest lower bound,
a unique least upper bound.

Therefore:

(L,≤)(L,\le)(L,≤)

forms a bounded lattice.

Proof
Existence of Meets

Any two elements always share a greatest lower bound.

Examples:

KT∧KF=HKT \wedge KF = HKT∧KF=H KT∧U=UKT \wedge U = UKT∧U=U UH∧KF=KFUH \wedge KF = KFUH∧KF=KF

Therefore meets exist for all pairs.

Existence of Joins

Any two elements always share a least upper bound.

Examples:

U∨H=HU \vee H = HU∨H=H KT∨H=KTKT \vee H = KTKT∨H=KT KT∨KF=UHKT \vee KF = UHKT∨KF=UH

Therefore joins exist for all pairs.

Uniqueness

The ordering diagram imposes a unique least upper bound and unique greatest lower bound for every pair.

Thus both lattice requirements are satisfied.

□\square□
9. Horizon Principle

The key innovation of BHL is that unresolved propositions are not assigned contradictory truth values.

Instead they are placed in the horizon state:

HHH

A proposition belongs to the horizon whenever its evaluation requires crossing the current informational boundary.

10. Russell Classification Rule

Define a self-reference detector:

ρ(p)\rho(p)ρ(p)

such that:

ρ(p)=1\rho(p)=1ρ(p)=1

whenever evaluation of proposition ppp recursively depends upon itself.

The BHL self-reference axiom is:

ρ(p)=1⇒p=H\rho(p)=1 \Rightarrow p=Hρ(p)=1⇒p=H

Applied to Russell's set:

R={x:x∉x}R=\{x:x\notin x\}R={x:x∈/x}

the statement

R∈RR\in RR∈R

becomes:

R∈R=HR\in R = HR∈R=H

Thus the paradox is classified as a horizon proposition rather than generating logical explosion.

11. Universal Horizon Interpretation

The Universal Horizon is not interpreted as a conventional universal set.

Instead:

UHUHUH

represents the space of all possible distinguishable boundary systems.

This avoids treating "everything" as a single object while preserving maximal closure of the logic.

12. Future Work

Potential future developments include:

Horizon Modal Logic
Boundary Semantics
BHL Proof Theory
Horizon-Valued Predicate Logic
Boundary Category Theory
Formal Treatment of Gödel Sentences
Formal Treatment of the Liar Paradox
Computational Models of Boundary Evolution
Horizon Differentiation Operators
Boundary-Horizon Topology
Summary

Boundary-Horizon Logic extends the BHF framework by introducing an informational truth space ordered by distinguishability. The addition of the Universal Horizon completes the structure, yielding a bounded lattice:

Plain Text
UH
/ \
KT KF
\ /
H
|
U
|
X

This lattice provides a mathematical foundation for reasoning about knowledge, uncertainty, self-reference, and informational boundaries within the Boundary-Horizon-Finitude framework.
