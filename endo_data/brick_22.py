BRICK = {
    "brick_num": 22,
    "brick_title": "Catecholamine Excess and Endocrine Hypertension: Pheochromocytoma and Paraganglioma",
    "games": [
        {
            "slug": "catecholamine_pathway",
            "title": "Catecholamine Synthesis and Metabolism",
            "subtitle": "Match each enzyme to its substrate, its product, and the point worth remembering",
            "categories": ["Substrate", "Product", "High-yield point"],
            "data": {
                "Tyrosine hydroxylase": {
                    "Substrate": "Tyrosine, the amino acid precursor of all catecholamines",
                    "Product": "L-3,4-dihydroxyphenylalanine (L-DOPA)",
                    "High-yield point": "Catalyzes the rate-limiting step of catecholamine synthesis"
                },
                "Aromatic L-amino acid decarboxylase": {
                    "Substrate": "L-DOPA",
                    "Product": "Dopamine",
                    "High-yield point": "Second synthetic step, immediately after tyrosine hydroxylase"
                },
                "Dopamine beta-hydroxylase": {
                    "Substrate": "Dopamine",
                    "Product": "Norepinephrine",
                    "High-yield point": "Works inside the secretory granules themselves"
                },
                "Phenylethanolamine N-methyltransferase": {
                    "Substrate": "Norepinephrine",
                    "Product": "Epinephrine",
                    "High-yield point": "Stimulated by high local cortisol exposure in the adrenal medulla"
                },
                "Catechol-O-methyltransferase": {
                    "Substrate": "Norepinephrine and epinephrine after they are made",
                    "Product": "Normetanephrine and metanephrine",
                    "High-yield point": "Intratumoral activity is continuous, so metanephrines are the screening test"
                }
            }
        },
        {
            "slug": "ppgl_tumor_types",
            "title": "Pheochromocytoma vs Sympathetic vs Parasympathetic Paraganglioma",
            "subtitle": "Sort each feature under the neural crest-derived tumor it describes",
            "categories": ["Pheochromocytoma", "Sympathetic paraganglioma", "Parasympathetic paraganglioma"],
            "data": {
                "Site of origin": {
                    "Pheochromocytoma": "Chromaffin cells of the adrenal medulla",
                    "Sympathetic paraganglioma": "Extra-adrenal paraganglia of thorax, abdomen, or pelvis",
                    "Parasympathetic paraganglioma": "Paraganglia of the head and neck"
                },
                "Secretory phenotype": {
                    "Pheochromocytoma": "Epinephrine, norepinephrine, or both",
                    "Sympathetic paraganglioma": "Often catecholamine-secreting, norepinephrine predominant",
                    "Parasympathetic paraganglioma": "Usually nonsecretory"
                },
                "Usual presentation": {
                    "Pheochromocytoma": "Episodic or sustained hypertension with headache, palpitations, diaphoresis",
                    "Sympathetic paraganglioma": "Catecholamine excess arising from a mass below the diaphragm",
                    "Parasympathetic paraganglioma": "Local mass effect rather than adrenergic spells"
                },
                "Typical biochemical clue": {
                    "Pheochromocytoma": "Metanephrine elevation, indicating epinephrine production",
                    "Sympathetic paraganglioma": "Normetanephrine-predominant elevation",
                    "Parasympathetic paraganglioma": "Metanephrines are commonly normal"
                },
                "Imaging emphasis": {
                    "Pheochromocytoma": "Contrast-enhanced CT of abdomen and pelvis after biochemical confirmation",
                    "Sympathetic paraganglioma": "Functional imaging added because disease is extra-adrenal",
                    "Parasympathetic paraganglioma": "MRI and MR angiography for skull base and cranial nerve relationships"
                }
            }
        },
        {
            "slug": "endocrine_hypertension_workup",
            "title": "Pattern Recognition in Endocrine Hypertension",
            "subtitle": "Match each endocrine cause of hypertension to its mediator, its pattern, and the first test to order",
            "categories": ["Hormone in excess", "Clinical pattern", "Initial biochemical test"],
            "data": {
                "Pheochromocytoma or paraganglioma": {
                    "Hormone in excess": "Catecholamines",
                    "Clinical pattern": "Paroxysmal headache, palpitations, diaphoresis, labile hypertension",
                    "Initial biochemical test": "Plasma free or 24-hour urinary fractionated metanephrines"
                },
                "Primary aldosteronism": {
                    "Hormone in excess": "Aldosterone",
                    "Clinical pattern": "Hypertension with unexplained hypokalemia",
                    "Initial biochemical test": "Aldosterone, renin, and the aldosterone-to-renin ratio"
                },
                "Cortisol excess": {
                    "Hormone in excess": "Cortisol",
                    "Clinical pattern": "Hypertension with features of glucocorticoid excess",
                    "Initial biochemical test": "Dexamethasone suppression, late-night salivary cortisol, or urinary free cortisol"
                },
                "Thyroid disease": {
                    "Hormone in excess": "Thyroid hormone",
                    "Clinical pattern": "Hypertension with tachycardia and other features of thyroid dysfunction",
                    "Initial biochemical test": "Thyroid-stimulating hormone with thyroid hormone testing"
                },
                "Acromegaly": {
                    "Hormone in excess": "Growth hormone",
                    "Clinical pattern": "Hypertension with features of growth hormone excess",
                    "Initial biochemical test": "Insulin-like growth factor 1"
                }
            }
        },
        {
            "slug": "ppgl_safe_management",
            "title": "Preparing a Functional PPGL Safely",
            "subtitle": "Match each step to its rationale, its place in the plan, and the danger of getting the order wrong",
            "categories": ["Physiologic rationale", "Where it belongs in the plan", "Danger if the sequence is ignored"],
            "data": {
                "Alpha-adrenergic blockade": {
                    "Physiologic rationale": "Opposes alpha-1-mediated arteriolar and venous vasoconstriction",
                    "Where it belongs in the plan": "Started at least 7 to 14 days before planned surgery",
                    "Danger if the sequence is ignored": "An unprepared patient can suffer intraoperative crisis or collapse"
                },
                "Sodium and volume repletion": {
                    "Physiologic rationale": "Corrects the chronic volume contraction of catecholamine excess",
                    "Where it belongs in the plan": "Alongside alpha blockade during preoperative preparation",
                    "Danger if the sequence is ignored": "Postoperative hypotension is more severe and harder to treat"
                },
                "Beta-adrenergic blockade": {
                    "Physiologic rationale": "Controls tachycardia and arrhythmia driven by beta-1 activation",
                    "Where it belongs in the plan": "Only after adequate alpha blockade, and only if tachycardia persists",
                    "Danger if the sequence is ignored": "Given first, it leaves alpha-mediated vasoconstriction unopposed"
                },
                "Biopsy of an adrenal mass": {
                    "Physiologic rationale": "Adds little before hormonal evaluation has been completed",
                    "Where it belongs in the plan": "Selected cases only, after pheochromocytoma is biochemically excluded",
                    "Danger if the sequence is ignored": "Tumor puncture can provoke abrupt catecholamine release"
                },
                "Care after tumor removal": {
                    "Physiologic rationale": "Circulating catecholamines fall abruptly once the tumor is gone",
                    "Where it belongs in the plan": "Monitored recovery immediately following resection",
                    "Danger if the sequence is ignored": "Hypotension and hypoglycemia as insulin inhibition resolves"
                }
            }
        }
    ]
}
