BRICK = {
    "brick_num": 40,
    "brick_title": "Micturition",
    "games": [
        {
            "slug": "bladder_receptors",
            "title": "Bladder Receptor Signaling",
            "subtitle": "Match each receptor to its location, signaling mechanism, and effect",
            "categories": ["Location and input", "Signaling mechanism", "Effect"],
            "data": {
                "Beta-3 adrenergic receptor": {
                    "Location and input": "Detrusor; sympathetic norepinephrine",
                    "Signaling mechanism": "Activates adenylyl cyclase, increasing cAMP",
                    "Effect": "Smooth muscle relaxation for low-pressure filling"
                },
                "Alpha-1 adrenergic receptor": {
                    "Location and input": "Internal urethral sphincter; sympathetic norepinephrine",
                    "Signaling mechanism": "Gq/IP3 signaling",
                    "Effect": "IUS contraction that maintains outlet resistance"
                },
                "M3 muscarinic receptor": {
                    "Location and input": "Detrusor; parasympathetic acetylcholine (primary driver)",
                    "Signaling mechanism": "Gq/phospholipase C, raising intracellular calcium",
                    "Effect": "Sustained detrusor contraction to drive voiding"
                },
                "M2 muscarinic receptor": {
                    "Location and input": "Detrusor; parasympathetic acetylcholine (amplifier)",
                    "Signaling mechanism": "Inhibits cAMP-mediated relaxation",
                    "Effect": "Amplifies detrusor contraction during voiding"
                },
                "Nicotinic ACh receptor": {
                    "Location and input": "External urethral sphincter striated muscle; pudendal nerve",
                    "Signaling mechanism": "Acetylcholine acts directly on the striated muscle",
                    "Effect": "EUS contraction that preserves continence during storage"
                }
            }
        },
        {
            "slug": "control_loop_centers",
            "title": "The Micturition Control Loop",
            "subtitle": "Match each neural structure to its location, role, and key feature",
            "categories": ["Location", "Role in the loop", "Key feature"],
            "data": {
                "A-delta stretch afferents": {
                    "Location": "Bladder wall, traveling in the pelvic nerve",
                    "Role in the loop": "Detect stretch, encoding bladder volume and wall tension",
                    "Key feature": "Myelinated fibers that transmit rapidly to the spinal cord"
                },
                "Periaqueductal gray (PAG)": {
                    "Location": "Midbrain",
                    "Role in the loop": "Relay and integrator that gates the voiding signal by context",
                    "Key feature": "Receives fullness signals plus prefrontal and limbic input"
                },
                "Pontine micturition center (PMC)": {
                    "Location": "Dorsal pons (Barrington's nucleus)",
                    "Role in the loop": "Master switch that triggers coordinated voiding",
                    "Key feature": "Excites sacral parasympathetics while inhibiting Onuf's nucleus"
                },
                "Prefrontal and anterior cingulate cortex": {
                    "Location": "Cerebral cortex",
                    "Role in the loop": "Tonic inhibition of the PAG-PMC pathway during storage",
                    "Key feature": "Raises the voiding threshold; decides to void or defer"
                },
                "Onuf's nucleus": {
                    "Location": "Sacral spinal cord (S2-S4)",
                    "Role in the loop": "Origin of pudendal motor neurons that contract the EUS",
                    "Key feature": "Suppressed by the PMC so the EUS relaxes during voiding"
                }
            }
        },
        {
            "slug": "nerves_of_bladder",
            "title": "Nerves of Bladder Control",
            "subtitle": "Match each nerve to its origin, chemical signal, and action",
            "categories": ["Origin", "Signal", "Action"],
            "data": {
                "Hypogastric nerve (sympathetic)": {
                    "Origin": "Spinal levels T10-L2",
                    "Signal": "Norepinephrine onto beta-3 and alpha-1 receptors",
                    "Action": "Storage: relaxes detrusor and contracts internal sphincter"
                },
                "Pelvic nerve (parasympathetic)": {
                    "Origin": "Sacral levels S2-S4",
                    "Signal": "Acetylcholine onto M3 and M2 muscarinic receptors",
                    "Action": "Voiding: drives sustained detrusor contraction"
                },
                "Pudendal nerve (somatic)": {
                    "Origin": "Onuf's nucleus at S2-S4",
                    "Signal": "Acetylcholine onto nicotinic receptors",
                    "Action": "Contracts the EUS; primary site of voluntary continence"
                },
                "A-delta afferent fibers (sensory)": {
                    "Origin": "Bladder wall",
                    "Signal": "Rapid stretch signals encoding volume and wall tension",
                    "Action": "Ascend to supraspinal centers to initiate the voiding reflex"
                }
            }
        },
        {
            "slug": "reflexes_and_dysfunction",
            "title": "Reflexes, Control, and Dysfunction",
            "subtitle": "Match each phenomenon to its mechanism, result, and level of control",
            "categories": ["Mechanism", "Result", "Level of neural control"],
            "data": {
                "Guarding reflex": {
                    "Mechanism": "Bladder afferents activate pudendal motor neurons via sacral interneurons",
                    "Result": "EUS tone rises with bladder pressure, preserving continence when coughing",
                    "Level of neural control": "Spinal loop, independent of supraspinal control"
                },
                "Voluntary deferral of voiding": {
                    "Mechanism": "Prefrontal and anterior cingulate cortex tonically inhibit PAG-PMC",
                    "Result": "Bladder fills beyond the point where stretch afferents first fire",
                    "Level of neural control": "Cortical, shaped by social context and prior experience"
                },
                "Detrusor-sphincter dyssynergia": {
                    "Mechanism": "Incomplete suppression of sympathetic or pudendal activity during voiding",
                    "Result": "Incomplete bladder emptying or obstructed voiding",
                    "Level of neural control": "Failed brainstem coordination of the storage-voiding switch"
                },
                "Detrusor overactivity": {
                    "Mechanism": "Involuntary detrusor contractions before normal bladder capacity",
                    "Result": "Urgency and leakage as contractions overwhelm sphincter resistance",
                    "Level of neural control": "Parasympathetic overactivity or detrusor hypersensitivity"
                }
            }
        }
    ]
}
