BRICK = {
    "brick_num": 4,
    "brick_title": "Hypothalamic-Pituitary (H-P) Axis 1",
    "games": [
        {
            "slug": "anterior_pituitary_axes",
            "title": "Anterior Pituitary Hormones and Their Axes",
            "subtitle": "Match each anterior pituitary hormone to its hypothalamic control, target, target hormone, and key function",
            "categories": ["Hypothalamic control", "Target gland or organ", "Target hormone", "Key function"],
            "data": {
                "Thyroid-stimulating hormone (TSH)": {
                    "Hypothalamic control": "Stimulated by thyrotropin-releasing hormone (TRH)",
                    "Target gland or organ": "Thyroid gland",
                    "Target hormone": "T3 and T4",
                    "Key function": "Sets basal metabolic rate in virtually all tissues"
                },
                "Adrenocorticotropic hormone (ACTH)": {
                    "Hypothalamic control": "Stimulated by corticotropin-releasing hormone (CRH)",
                    "Target gland or organ": "Adrenal cortex",
                    "Target hormone": "Cortisol",
                    "Key function": "Maintains blood pressure, blood glucose, and the stress response"
                },
                "LH and FSH": {
                    "Hypothalamic control": "Stimulated by gonadotropin-releasing hormone (GnRH)",
                    "Target gland or organ": "Ovaries and testes",
                    "Target hormone": "Estradiol and testosterone",
                    "Key function": "Controls reproduction and secondary sex characteristics"
                },
                "Growth hormone (GH)": {
                    "Hypothalamic control": "Stimulated by growth hormone-releasing hormone (GHRH)",
                    "Target gland or organ": "Liver, plus direct action on bone and muscle",
                    "Target hormone": "IGF-1, alongside direct GH action",
                    "Key function": "Drives bone growth and increases muscle mass"
                },
                "Prolactin": {
                    "Hypothalamic control": "Tonically inhibited by dopamine rather than stimulated",
                    "Target gland or organ": "Breast",
                    "Target hormone": "None; prolactin itself is the effector hormone",
                    "Key function": "Stimulates milk production during lactation"
                }
            }
        },
        {
            "slug": "anterior_vs_posterior",
            "title": "Two Glands Fused Into One",
            "subtitle": "Sort each structural feature under the lobe of the pituitary it describes",
            "categories": ["Anterior pituitary", "Posterior pituitary"],
            "data": {
                "Tissue of origin": {
                    "Anterior pituitary": "Glandular epithelium",
                    "Posterior pituitary": "Hypothalamic neural tissue"
                },
                "Route of the signal from the hypothalamus": {
                    "Anterior pituitary": "Releasing hormones carried by hypophyseal portal vessels",
                    "Posterior pituitary": "Direct axonal transport through the infundibulum"
                },
                "Where its hormones are synthesized": {
                    "Anterior pituitary": "In the pituitary cells that secrete the tropic hormones",
                    "Posterior pituitary": "In hypothalamic supraoptic and paraventricular neurons"
                },
                "Number of steps to reach the effect": {
                    "Anterior pituitary": "Three tiers, with signal amplification at each step",
                    "Posterior pituitary": "One step, because the hypothalamic neuron is the gland"
                },
                "Hormones released": {
                    "Anterior pituitary": "FSH, LH, ACTH, TSH, prolactin, and GH",
                    "Posterior pituitary": "Oxytocin and vasopressin (ADH)"
                }
            }
        },
        {
            "slug": "failure_level_map",
            "title": "Failure-Level Map on the Cortisol Axis",
            "subtitle": "Sort each feature under the hormone pattern it belongs to",
            "categories": ["Primary failure", "Secondary failure", "Primary overproduction", "Secondary overproduction"],
            "data": {
                "Plasma ACTH": {
                    "Primary failure": "High, because the intact pituitary is compensating",
                    "Secondary failure": "Inappropriately normal or low, with no compensation",
                    "Primary overproduction": "Low, because feedback has suppressed it",
                    "Secondary overproduction": "High, because the pituitary is driving the axis"
                },
                "Serum cortisol": {
                    "Primary failure": "Low despite maximal pituitary drive",
                    "Secondary failure": "Low because the adrenal is never stimulated",
                    "Primary overproduction": "High and made independently of ACTH",
                    "Secondary overproduction": "High and made in response to excess ACTH"
                },
                "Tier that has failed": {
                    "Primary failure": "Target gland, with hypothalamus and pituitary intact",
                    "Secondary failure": "Anterior pituitary, which cannot make tropic hormone",
                    "Primary overproduction": "Target gland, escaping all upstream control",
                    "Secondary overproduction": "Anterior pituitary, generating an unregulated signal"
                },
                "Classic example": {
                    "Primary failure": "Addison disease",
                    "Secondary failure": "Pituitary tumor or surgical damage to the pituitary",
                    "Primary overproduction": "Cortisol-secreting adrenal tumor",
                    "Secondary overproduction": "Cushing disease from a corticotroph adenoma"
                },
                "What the tropic hormone tells you": {
                    "Primary failure": "It rose appropriately, so look below the pituitary",
                    "Secondary failure": "It failed to rise, so the lesion is at the pituitary",
                    "Primary overproduction": "It was suppressed, so the excess starts downstream",
                    "Secondary overproduction": "It is high alongside the target hormone, so the pituitary is the source"
                }
            }
        },
        {
            "slug": "localize_the_lesion",
            "title": "Reading the Pattern to Localize the Lesion",
            "subtitle": "Match each clinical picture to the pattern it shows, the level that failed, and the explanation",
            "categories": ["Hormone pattern", "Level that has failed", "Explanation"],
            "data": {
                "Low free T4 with high TSH": {
                    "Hormone pattern": "Target hormone low while the tropic hormone rises",
                    "Level that has failed": "Thyroid gland, the tier 3 target",
                    "Explanation": "Primary hypothyroidism; an intact pituitary is compensating"
                },
                "Low free T4 with low TSH": {
                    "Hormone pattern": "Target hormone and tropic hormone both low together",
                    "Level that has failed": "Anterior pituitary, the tier 2 relay",
                    "Explanation": "Secondary hypothyroidism; the pituitary never compensates"
                },
                "High free T4 with undetectable TSH and stimulating antibodies": {
                    "Hormone pattern": "Target hormone high while the tropic hormone is suppressed",
                    "Level that has failed": "Thyroid gland, driven from outside the axis",
                    "Explanation": "Graves disease; feedback works but cannot silence the antibody"
                },
                "Rising prolactin while TSH, ACTH, LH, FSH, and GH all fall": {
                    "Hormone pattern": "One hormone moving opposite to all the others",
                    "Level that has failed": "The stalk connection between hypothalamus and pituitary",
                    "Explanation": "Lost dopamine inhibition raises prolactin as stimulation disappears"
                },
                "Polyuria with dilute urine and intact thirst after head trauma": {
                    "Hormone pattern": "No tropic hormone exists to measure at all",
                    "Level that has failed": "Posterior pituitary release of ADH",
                    "Explanation": "Central diabetes insipidus; three-tier localization does not apply"
                },
                "Failed postpartum lactation with every anterior tropic hormone low": {
                    "Hormone pattern": "All tropic hormones and their targets low at once",
                    "Level that has failed": "The entire anterior pituitary",
                    "Explanation": "Sheehan syndrome infarction, with the posterior lobe typically spared"
                }
            }
        }
    ]
}
