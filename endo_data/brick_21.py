BRICK = {
    "brick_num": 21,
    "brick_title": "Adrenal Steroid Biosynthesis and Regulation: Zones, Pathways, and Enzyme Deficiencies",
    "games": [
        {
            "slug": "adrenal_zones",
            "title": "Zones of the Adrenal Gland",
            "subtitle": "Match each adrenal layer to its dominant product, its main regulator, and a defining feature",
            "categories": ["Dominant product", "Main regulatory input", "Defining feature"],
            "data": {
                "Zona glomerulosa": {
                    "Dominant product": "Aldosterone, the adrenal mineralocorticoid",
                    "Main regulatory input": "Angiotensin II and serum potassium, not ACTH",
                    "Defining feature": "Lacks CYP17A1, so flux is pushed toward aldosterone"
                },
                "Zona fasciculata": {
                    "Dominant product": "Cortisol, the adrenal glucocorticoid",
                    "Main regulatory input": "ACTH from the hypothalamic-pituitary-adrenal axis",
                    "Defining feature": "Expresses CYP17A1, CYP21A2, and CYP11B1 together"
                },
                "Zona reticularis": {
                    "Dominant product": "Adrenal androgens, mainly DHEA and androstenedione",
                    "Main regulatory input": "ACTH-driven substrate delivery with no dedicated tropic hormone",
                    "Defining feature": "CYP17A1 biased toward 17,20-lyase activity by cytochrome b5"
                },
                "Adrenal medulla": {
                    "Dominant product": "Catecholamines, chiefly epinephrine and norepinephrine",
                    "Main regulatory input": "Preganglionic sympathetic cholinergic fibers",
                    "Defining feature": "Neural crest chromaffin cells; cortical cortisol induces PNMT"
                }
            }
        },
        {
            "slug": "steroidogenic_enzymes",
            "title": "Enzymes of Adrenal Steroidogenesis",
            "subtitle": "Place each protein with the step it drives, where it acts, and what happens when it fails",
            "categories": ["Step catalyzed", "Where it matters", "Effect of deficiency or blockade"],
            "data": {
                "StAR protein": {
                    "Step catalyzed": "Transports cholesterol into the mitochondrion",
                    "Where it matters": "First committed step, shared by all three cortical zones",
                    "Effect of deficiency or blockade": "Aldosterone, cortisol, and androgen output all fall at once"
                },
                "CYP11A1": {
                    "Step catalyzed": "Cleaves the cholesterol side chain to make pregnenolone",
                    "Where it matters": "Common entry reaction before any zone-specific branching",
                    "Effect of deficiency or blockade": "No pregnenolone, so every downstream steroid branch is starved"
                },
                "CYP17A1 (17alpha-hydroxylase / 17,20-lyase)": {
                    "Step catalyzed": "Adds a 17-hydroxyl group and can cleave the 17,20 bond",
                    "Where it matters": "Fasciculata and reticularis; absent from the glomerulosa",
                    "Effect of deficiency or blockade": "Cortisol and sex steroids fall; hypertension with androgen deficiency"
                },
                "CYP21A2 (21-hydroxylase)": {
                    "Step catalyzed": "Progesterone to DOC and 17-hydroxyprogesterone to 11-deoxycortisol",
                    "Where it matters": "Required by the mineralocorticoid and glucocorticoid branches alike",
                    "Effect of deficiency or blockade": "Salt wasting with androgen excess, the classic severe CAH"
                },
                "CYP11B1 (11beta-hydroxylase)": {
                    "Step catalyzed": "Converts 11-deoxycortisol to cortisol",
                    "Where it matters": "Terminal glucocorticoid enzyme of the zona fasciculata",
                    "Effect of deficiency or blockade": "DOC accumulates, giving hypertension plus androgen excess"
                },
                "CYP11B2 (aldosterone synthase)": {
                    "Step catalyzed": "Completes conversion of corticosterone to aldosterone",
                    "Where it matters": "Terminal mineralocorticoid enzyme of the zona glomerulosa",
                    "Effect of deficiency or blockade": "Mineralocorticoid output fails without disturbing cortisol"
                }
            }
        },
        {
            "slug": "zone_selective_regulation",
            "title": "Cortisol vs Aldosterone vs Adrenal Androgens",
            "subtitle": "Sort each regulatory feature under the adrenal output it controls",
            "categories": ["Cortisol", "Aldosterone", "Adrenal androgens"],
            "data": {
                "Dominant stimulus": {
                    "Cortisol": "CRH then ACTH along the hypothalamic-pituitary-adrenal axis",
                    "Aldosterone": "Renin-angiotensin-aldosterone system plus serum potassium",
                    "Adrenal androgens": "ACTH-dependent substrate delivery with no LH/FSH equivalent"
                },
                "Cellular signaling detail": {
                    "Cortisol": "ACTH binds MC2R; cAMP signaling that needs the MRAP accessory protein",
                    "Aldosterone": "Angiotensin II raises intracellular calcium and induces CYP11B2",
                    "Adrenal androgens": "17,20-lyase activity of CYP17A1, augmented by cytochrome b5"
                },
                "Restraining or opposing signal": {
                    "Cortisol": "Cortisol feeds back to suppress hypothalamic CRH and pituitary ACTH",
                    "Aldosterone": "Atrial natriuretic peptide suppresses synthesis during volume expansion",
                    "Adrenal androgens": "No dedicated feedback loop; flux is set by reticularis programming"
                },
                "When output rises": {
                    "Cortisol": "Early morning peak, plus acute stress, hypoglycemia, and IL-1/IL-6/TNF-alpha",
                    "Aldosterone": "Low renal perfusion, low distal sodium delivery, or hyperkalemia",
                    "Adrenal androgens": "Adrenarche in mid-childhood as the reticularis matures"
                },
                "Effect of losing ACTH drive": {
                    "Cortisol": "Output falls quickly and the fasciculata atrophies over time",
                    "Aldosterone": "Largely preserved, since ACTH is only a minor transient stimulus",
                    "Adrenal androgens": "DHEA and DHEA-S fall as the reticularis loses trophic support"
                }
            }
        },
        {
            "slug": "cah_enzyme_blocks",
            "title": "Congenital Adrenal Hyperplasia Blocks",
            "subtitle": "Sort each finding under the enzyme deficiency that produces it",
            "categories": ["21-hydroxylase deficiency", "11beta-hydroxylase deficiency", "17alpha-hydroxylase deficiency"],
            "data": {
                "Cortisol synthesis": {
                    "21-hydroxylase deficiency": "Impaired, so ACTH rises and the cortex hyperplasias",
                    "11beta-hydroxylase deficiency": "Impaired at the final step from 11-deoxycortisol",
                    "17alpha-hydroxylase deficiency": "Impaired because 17-hydroxylated intermediates cannot form"
                },
                "Mineralocorticoid status": {
                    "21-hydroxylase deficiency": "Aldosterone synthesis also blocked, producing salt wasting",
                    "11beta-hydroxylase deficiency": "DOC accumulates and acts as a mineralocorticoid",
                    "17alpha-hydroxylase deficiency": "DOC and corticosterone drive mineralocorticoid excess"
                },
                "Adrenal androgen output": {
                    "21-hydroxylase deficiency": "Increased, as blocked precursors are diverted to androgens",
                    "11beta-hydroxylase deficiency": "Increased, giving virilization alongside the enzyme block",
                    "17alpha-hydroxylase deficiency": "Decreased, since androgens need CYP17A1 to be made"
                },
                "Blood pressure and volume": {
                    "21-hydroxylase deficiency": "Hypotension and dehydration from salt loss",
                    "11beta-hydroxylase deficiency": "Hypertension from retained sodium and volume",
                    "17alpha-hydroxylase deficiency": "Hypertension from sustained mineralocorticoid activity"
                },
                "Classic presentation": {
                    "21-hydroxylase deficiency": "Vomiting, lethargic newborn with hyponatremia and hyperkalemia",
                    "11beta-hydroxylase deficiency": "Child with early pubic hair and elevated blood pressure",
                    "17alpha-hydroxylase deficiency": "Teen with primary amenorrhea and absent secondary sexual development"
                }
            }
        }
    ]
}
