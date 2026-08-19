BRICK = {
    "brick_num": 12,
    "brick_title": "Thyroid Hormone Synthesis, Regulation, and Testing",
    "games": [
        {
            "slug": "synthesis_steps",
            "title": "Steps of Thyroid Hormone Synthesis",
            "subtitle": "Match each step to what it accomplishes, the protein that carries it out, and where it happens",
            "categories": ["What happens", "Key protein or enzyme", "Where it happens"],
            "data": {
                "Iodide trapping": {
                    "What happens": "Iodide is pulled out of the blood into the follicular cell",
                    "Key protein or enzyme": "Sodium-iodide symporter",
                    "Where it happens": "Basolateral membrane of the follicular cell"
                },
                "Oxidation and organification": {
                    "What happens": "Iodine is attached to tyrosine residues, forming MIT and DIT",
                    "Key protein or enzyme": "Thyroid peroxidase, oxidizing iodide first",
                    "Where it happens": "Apical surface, where the cell meets colloid"
                },
                "Coupling": {
                    "What happens": "MIT plus DIT yields T3; DIT plus DIT yields T4",
                    "Key protein or enzyme": "Thyroid peroxidase again, now joining iodotyrosines",
                    "Where it happens": "On the thyroglobulin scaffold at the apical membrane"
                },
                "Storage": {
                    "What happens": "Preformed hormone is held as a reserve pool",
                    "Key protein or enzyme": "Thyroglobulin, the protein hormone stays attached to",
                    "Where it happens": "Colloid, the central space of the follicle"
                },
                "Endocytosis and proteolysis": {
                    "What happens": "Iodinated scaffold is retrieved and digested, freeing T4 and T3",
                    "Key protein or enzyme": "Thyroid-stimulating hormone triggers it; lysosomal enzymes do it",
                    "Where it happens": "Inside the follicular cell, in lysosomes"
                }
            }
        },
        {
            "slug": "hormone_forms",
            "title": "T4, T3, Reverse T3, and Their Precursors",
            "subtitle": "Match each molecule to where it is made, how it is made, and what it does",
            "categories": ["Where it is made", "How it is made", "Biologic activity"],
            "data": {
                "Thyroxine (T4)": {
                    "Where it is made": "Secreted directly by the thyroid gland as its main product",
                    "How it is made": "Two DIT residues coupled by thyroid peroxidase",
                    "Biologic activity": "Prohormone; much of its effect depends on conversion to T3"
                },
                "Triiodothyronine (T3)": {
                    "Where it is made": "Mostly peripheral tissues, with a smaller amount from the gland",
                    "How it is made": "MIT plus DIT in the gland; deiodination of T4 in tissues",
                    "Biologic activity": "The more active hormone at thyroid hormone receptors"
                },
                "Reverse T3": {
                    "Where it is made": "Peripheral tissues, from circulating thyroxine",
                    "How it is made": "Alternate deiodination of T4 by deiodinase enzymes",
                    "Biologic activity": "Inactive; rises in acute illness, starvation, or severe stress"
                },
                "Monoiodotyrosine (MIT)": {
                    "Where it is made": "On thyroglobulin, at the apical face of the follicular cell",
                    "How it is made": "One iodine attached to a tyrosine residue",
                    "Biologic activity": "Not a hormone; couples with DIT to build T3"
                },
                "Diiodotyrosine (DIT)": {
                    "Where it is made": "On thyroglobulin stored in the colloid",
                    "How it is made": "Two iodines attached to a tyrosine residue",
                    "Biologic activity": "Not a hormone; two of them couple to build T4"
                }
            }
        },
        {
            "slug": "axis_failure_map",
            "title": "Reading the Thyroid Axis Failure Map",
            "subtitle": "Match each pattern to its TSH, its free hormone levels, and where the axis has failed",
            "categories": ["TSH", "Free hormone levels", "Where the problem is"],
            "data": {
                "Primary hypothyroidism": {
                    "TSH": "Elevated",
                    "Free hormone levels": "Free T4 low",
                    "Where the problem is": "Thyroid gland underproduces; the pituitary responds appropriately"
                },
                "Primary hyperthyroidism": {
                    "TSH": "Low",
                    "Free hormone levels": "Free T4 and/or free T3 high",
                    "Where the problem is": "Thyroid gland makes hormone in excess of what the axis asks for"
                },
                "Central hypothyroidism": {
                    "TSH": "Low or inappropriately normal",
                    "Free hormone levels": "Free T4 low",
                    "Where the problem is": "Hypothalamus or pituitary fails to drive a capable gland"
                },
                "TSH-secreting pituitary adenoma": {
                    "TSH": "Normal or high when it should be suppressed",
                    "Free hormone levels": "Free T4 and/or free T3 high",
                    "Where the problem is": "Pituitary drives the gland despite negative feedback"
                },
                "Nonthyroidal illness syndrome": {
                    "TSH": "Normal or low during the illness",
                    "Free hormone levels": "T3 low, free T4 normal or low, reverse T3 up",
                    "Where the problem is": "Illness alters deiodination and central signaling, not the gland"
                }
            }
        },
        {
            "slug": "binding_proteins",
            "title": "Binding Proteins Versus True Thyroid Disease",
            "subtitle": "Sort each laboratory feature under the state it belongs to",
            "categories": ["Increased thyroid-binding globulin", "Decreased binding proteins", "Primary hypothyroidism"],
            "data": {
                "Total T4 and total T3": {
                    "Increased thyroid-binding globulin": "Increased, because more hormone is protein-bound",
                    "Decreased binding proteins": "Decreased, because there is less protein to carry hormone",
                    "Primary hypothyroidism": "Low, because the gland is making less hormone"
                },
                "Free T4": {
                    "Increased thyroid-binding globulin": "Usually normal; binding changes do not create hormone",
                    "Decreased binding proteins": "Normal, since biologically available hormone is preserved",
                    "Primary hypothyroidism": "Low, reflecting a true hormone deficiency"
                },
                "TSH": {
                    "Increased thyroid-binding globulin": "Normal, though early pregnancy hCG can lower it slightly",
                    "Decreased binding proteins": "Normal, because feedback sees normal free hormone",
                    "Primary hypothyroidism": "Elevated, as the pituitary tries to drive the gland"
                },
                "Typical cause": {
                    "Increased thyroid-binding globulin": "Pregnancy or estrogen therapy",
                    "Decreased binding proteins": "Androgens, severe liver disease, nephrotic protein loss, drugs",
                    "Primary hypothyroidism": "Disease of the thyroid gland itself"
                },
                "Correct interpretation": {
                    "Increased thyroid-binding globulin": "High total hormone without true hyperthyroidism",
                    "Decreased binding proteins": "Low total hormone without true hypothyroidism",
                    "Primary hypothyroidism": "Real hormone deficiency, confirmed by the free hormone level"
                }
            }
        }
    ]
}
