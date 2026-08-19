BRICK = {
    "brick_num": 10,
    "brick_title": "Hyperthyroidism and Thyroid Storm",
    "games": [
        {
            "slug": "causes_of_thyrotoxicosis",
            "title": "Causes of Thyrotoxicosis",
            "subtitle": "Match each cause to its mechanism, its radioactive iodine uptake pattern, and its bedside clue",
            "categories": ["Mechanism", "Radioactive iodine uptake", "Bedside clue"],
            "data": {
                "Graves disease": {
                    "Mechanism": "Thyroid-stimulating immunoglobulins activate the TSH receptor",
                    "Radioactive iodine uptake": "Diffuse increased uptake across the whole gland",
                    "Bedside clue": "Diffuse goiter with proptosis or pretibial dermopathy"
                },
                "Toxic multinodular goiter": {
                    "Mechanism": "Multiple autonomous nodules synthesize hormone on their own",
                    "Radioactive iodine uptake": "Patchy increased uptake in several irregular areas",
                    "Bedside clue": "Older patient with a longstanding nodular goiter"
                },
                "Toxic adenoma": {
                    "Mechanism": "One autonomous nodule synthesizes excess hormone",
                    "Radioactive iodine uptake": "Focal increased uptake with the rest of the gland suppressed",
                    "Bedside clue": "Single palpable nodule without eye or skin findings"
                },
                "Thyroiditis": {
                    "Mechanism": "Damaged follicles leak preformed stored hormone",
                    "Radioactive iodine uptake": "Low uptake despite florid biochemical thyrotoxicosis",
                    "Bedside clue": "Anterior neck pain, or onset after pregnancy or a drug"
                },
                "Exogenous thyroid hormone": {
                    "Mechanism": "Hormone comes from outside the gland; the gland is suppressed",
                    "Radioactive iodine uptake": "Low uptake because negative feedback shuts off trapping",
                    "Bedside clue": "No goiter, with access to or use of thyroid hormone"
                },
                "Central hyperthyroidism": {
                    "Mechanism": "Inappropriate pituitary TSH secretion drives the thyroid",
                    "Radioactive iodine uptake": "Increased uptake from ongoing central stimulation",
                    "Bedside clue": "TSH not suppressed even though free T4 is high"
                }
            }
        },
        {
            "slug": "high_versus_low_uptake",
            "title": "Sorting a Thyrotoxic Patient by Uptake",
            "subtitle": "Sort each feature under the state it belongs to",
            "categories": ["Graves disease", "Thyroiditis", "Exogenous hormone exposure"],
            "data": {
                "Is the gland synthesizing hormone?": {
                    "Graves disease": "Yes, true hyperthyroidism driven by receptor stimulation",
                    "Thyroiditis": "No, stored hormone is leaking from damaged follicles",
                    "Exogenous hormone exposure": "No, the gland is suppressed by negative feedback"
                },
                "Radioactive iodine uptake": {
                    "Graves disease": "Diffusely increased",
                    "Thyroiditis": "Low, because trapping is not driving the hormone excess",
                    "Exogenous hormone exposure": "Low, because the source bypasses the gland"
                },
                "Serum thyroglobulin": {
                    "Graves disease": "Made by an actively stimulated gland",
                    "Thyroiditis": "May be elevated as damaged follicles spill their contents",
                    "Exogenous hormone exposure": "Often low, since no endogenous hormone is released"
                },
                "Value of a thionamide": {
                    "Graves disease": "Useful, because it blocks the increased new synthesis",
                    "Thyroiditis": "Usually unhelpful, since new synthesis is not the problem",
                    "Exogenous hormone exposure": "Unhelpful, since the hormone is not made in the gland"
                },
                "Mechanism-matched treatment": {
                    "Graves disease": "Antithyroid drug, radioactive iodine, or surgery",
                    "Thyroiditis": "Supportive and anti-inflammatory therapy while the leak resolves",
                    "Exogenous hormone exposure": "Stop or reduce the outside source and control symptoms"
                }
            }
        },
        {
            "slug": "mechanism_based_treatment",
            "title": "Mechanism-Based Treatment of Thyrotoxicosis",
            "subtitle": "Match each treatment to what it does, when it is chosen, and its key caution",
            "categories": ["What it does", "When it is chosen", "Key caution"],
            "data": {
                "Beta-blocker": {
                    "What it does": "Blunts adrenergic effects: palpitations, tremor, anxiety, tachycardia",
                    "When it is chosen": "Any symptomatic thyrotoxicosis, whatever the cause",
                    "Key caution": "Controls symptoms only; it does not lower hormone levels"
                },
                "Thionamide": {
                    "What it does": "Inhibits thyroid peroxidase and blocks new hormone synthesis",
                    "When it is chosen": "Synthesis-driven states: Graves, toxic goiter, toxic adenoma",
                    "Key caution": "Takes time and does not remove stored or circulating hormone"
                },
                "Iodine in thyroid storm": {
                    "What it does": "Blocks release of hormone from the gland",
                    "When it is chosen": "Only after thionamide has been started in thyroid storm",
                    "Key caution": "Given first, it supplies substrate for new hormone synthesis"
                },
                "Glucocorticoids": {
                    "What it does": "Reduce peripheral T4-to-T3 conversion and support adrenal reserve",
                    "When it is chosen": "Part of the stacked regimen for thyroid storm",
                    "Key caution": "One layer of a stack, not a stand-alone therapy"
                },
                "Radioactive iodine or surgery": {
                    "What it does": "Definitively destroys or removes hyperfunctioning thyroid tissue",
                    "When it is chosen": "Selected synthesis-driven hyperthyroid states, non-urgently",
                    "Key caution": "Not emergency therapy and not used for a hormone leak"
                },
                "Anti-inflammatory supportive care": {
                    "What it does": "Treats the inflammation while preformed hormone washes out",
                    "When it is chosen": "Thyroiditis-related thyrotoxicosis with low uptake",
                    "Key caution": "Blocking synthesis instead misses the actual mechanism"
                }
            }
        },
        {
            "slug": "storm_versus_lookalikes",
            "title": "Thyroid Storm and Its Look-Alikes",
            "subtitle": "Sort each feature under the clinical state it belongs to",
            "categories": ["Thyroid storm", "Uncomplicated thyrotoxicosis", "Nonthyroidal illness syndrome"],
            "data": {
                "Defining feature": {
                    "Thyroid storm": "Multisystem decompensation: fever, agitation, cardiovascular instability",
                    "Uncomplicated thyrotoxicosis": "Excess hormone effect without systemic decompensation",
                    "Nonthyroidal illness syndrome": "Altered thyroid tests without primary thyroid disease"
                },
                "TSH pattern": {
                    "Thyroid storm": "Suppressed, but no lab value defines the emergency",
                    "Uncomplicated thyrotoxicosis": "Suppressed, which is what first flags the state",
                    "Nonthyroidal illness syndrome": "Normal or low during severe systemic illness"
                },
                "Thyroid hormone pattern": {
                    "Thyroid storm": "Free T4 elevated, though no threshold makes the diagnosis",
                    "Uncomplicated thyrotoxicosis": "Free T4 and/or free T3 clearly elevated",
                    "Nonthyroidal illness syndrome": "Low T3 with normal or low free T4; reverse T3 rises"
                },
                "Typical setting": {
                    "Thyroid storm": "Untreated thyrotoxicosis plus infection, surgery, trauma, or childbirth",
                    "Uncomplicated thyrotoxicosis": "Graves, nodular disease, thyroiditis, or exogenous hormone",
                    "Nonthyroidal illness syndrome": "Critically ill patient with no autonomous hormone production"
                },
                "Management priority": {
                    "Thyroid storm": "Stacked blockade plus treatment of the precipitating trigger",
                    "Uncomplicated thyrotoxicosis": "Identify the mechanism, then match therapy to it",
                    "Nonthyroidal illness syndrome": "Treat the underlying illness, not the thyroid number"
                }
            }
        }
    ]
}
