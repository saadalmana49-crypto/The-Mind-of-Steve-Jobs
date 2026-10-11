# Hardware and integrated systems

Use this for physical products, devices with companion apps or cloud services, and any product made of several parts that must feel like one: device + app + service + accessories + support.

## Own what determines the experience

Jobs described Apple as the last computer company that made "the whole widget" (WW03). At the iPhone launch he showed Alan Kay's line: "People who are really serious about software should make their own hardware" (IPH07).

The useful lesson is not "build everything yourself". It is this test for each component:

> If this part is mediocre, does the core experience suffer?

- **Yes:** own it or control it tightly. That means designing it, specifying it precisely, or choosing the supplier and testing it yourself. Typical examples: the primary input, the display, battery behavior, setup, and the sync that carries the user's data.
- **No:** use a good commodity part or standard, and spend the attention elsewhere.

## The system is the product

The iPod was a device, a desktop app (iTunes), a fast connection (FireWire: "1,000 songs in under ten minutes", IPOD01), and later a store. Each part was designed around the others.

Map your system before designing any one part:

```
Device ── companion app ── cloud service ── accessories
   │            │                │              │
packaging    app store       accounts       retail/support
   └──────── updates, data, identity flow between all of them ────────┘
```

For each handoff, ask:
- What does the user have to do here?
- What can fail?
- Who owns the fix?

Bad products feel coherent within each part and broken at the seams.

## Decide what is physical and what is software

- The iPhone replaced physical keyboards that were "there whether or not you need them" with software controls that adapt to each application (IPH07).
- Isaacson reports the iPod had no on/off switch. It slept and woke on its own (ISA11).

Rules of thumb:
- **Make it physical** when it must work blind, in a hurry, with gloves, or in an emergency. Also when status must be visible at a glance from across the room. Examples: power or mute, volume, the safety stop, a status light.
- **Make it software** when it changes by context, needs explanation, or will improve after launch.
- **Automate it away** when the right state is knowable: sleep and wake, updates, calibration, pairing.
- **Each physical control** should do one obvious thing. Hidden long-press combinations belong in the manual for recovery only, such as a factory reset.

## Out of the box to first value

Design this stretch as one continuous experience. Measure it in minutes and steps:
- **Opening the box shows the product first.** The packaging's job is to get the product into use, not to hold paperwork.
- **The device does something useful, or at least shows its state, before any app or account exists.** The app adds depth. It should not be the price of basic function.
- **Setup:**
  - one cable or none,
  - pairing without typing codes where the platform allows it,
  - credentials reused from the phone,
  - no account required for local core function,
  - clear status at every step.
- **Ship ready to use:** charged where possible, current firmware at first boot or updated silently, sensible defaults.
- **Set the target, then test it with people who have never seen the product.** For example: first value within 10 minutes of opening the box.

## Craft inside and out

"The quality has to be carried all the way through" (PB85). The Mac team's signatures were molded inside the case (FL-SIGN). For hardware, carrying quality through means:
- the internal layout,
- cable routing,
- the fit and finish of parts no one sees,
- tolerances,
- how it feels after a year of use.

Modern requirements add obligations the 1980s didn't have:
- **Repairability and replaceable batteries,** where regulations or the product's lifespan call for them.
- **Recyclable materials.**
- **Long-term software support.**

## Respect physics and manufacturing

Beauty must survive real use:
- **Test in real grips, rooms, and conditions.** The iPhone 4 put its antennas in the exterior band. Holding it a certain way reduced signal. Apple gave every owner a free case (AG10). Industrial design that touches function (radios, thermals, acoustics, sensors) must be validated in realistic use.
- **Fit the buyer's job and price.** Apple suspended the G4 Cube after a year. Its own press release said most customers bought the Power Mac G4 tower instead (CUBE01). The NeXT Computer was exquisite and priced far beyond much of its market, and NeXT left hardware in 1993.
- **Budget for reality:** thermals, battery capacity versus thinness, RF performance, drop tests, manufacturing yield, certification, supply. When design ambition conflicts with these, decide openly what the user gains and loses.

## Lifetime of the system

- **Firmware updates:** safe, automatic or one tap, and never bricking the device.
- **Offline behavior:** the core function keeps working without the cloud. Data is buffered and synced later.
- **Data ownership:** export, deletion, and a plain statement of what is collected.
- **End of life:** what the device still does if the company's service shuts down. Say so before purchase.
- **Many users and devices:** households, sharing, handing the device to a new owner, factory reset.

## Device, app, or service?

| Put it on the device | Put it in the app | Put it in the service |
|---|---|---|
| The one glanceable status | History, trends, explanations | Sync across devices and people |
| The most frequent action | Setup, configuration, advanced options | Backups, remote access |
| Safety-critical alerts | Notifications policy | Updates, fleet health |
| Works with no phone or network | Accounts, sharing, export | Anything that needs aggregation |

## Hardware checklist

- [ ] Purpose sentence written. The device does something useful without the app.
- [ ] Physical controls: each has one obvious job. The rest is software or automated.
- [ ] Out-of-box to first value: target set, steps counted, tested with newcomers.
- [ ] Every handoff (device ↔ app ↔ service) has its failure states designed.
- [ ] Validated in realistic use: grip, placement, temperature, network.
- [ ] Price and design fit the actual buyer's job.
- [ ] Update, offline, export, end-of-life, and resale paths defined.
- [ ] Accessibility: tactile and audible cues, readable status, app accessibility.
