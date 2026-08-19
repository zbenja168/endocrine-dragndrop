BRICK = {
    "brick_num": 16,
    "brick_title": "Thyroid Nodule Evaluation: TSH Testing, Ultrasound Risk Stratification, Fine-Needle Aspiration, and Bethesda Cytology",
    "games": [
        {
            "slug": "us_benign_vs_suspicious",
            "title": "Benign-Leaning vs Suspicious Ultrasound Patterns",
            "subtitle": "Sort each ultrasound descriptor under the risk pattern it belongs to",
            "categories": ["Benign-leaning pattern", "Suspicious pattern"],
            "data": {
                "Composition": {
                    "Benign-leaning pattern": "Purely cystic or spongiform composition",
                    "Suspicious pattern": "Solid hypoechoic or very hypoechoic composition"
                },
                "Margins": {
                    "Benign-leaning pattern": "Smooth, well-defined margins",
                    "Suspicious pattern": "Irregular, microlobulated, or infiltrative margins"
                },
                "Echogenic foci": {
                    "Benign-leaning pattern": "Comet-tail artifact arising from cystic spaces",
                    "Suspicious pattern": "Punctate echogenic foci within the nodule"
                },
                "Shape": {
                    "Benign-leaning pattern": "Wider-than-tall shape",
                    "Suspicious pattern": "Taller-than-wide shape"
                },
                "Surrounding structures": {
                    "Benign-leaning pattern": "No extrathyroidal extension and no suspicious cervical nodes",
                    "Suspicious pattern": "Extrathyroidal extension with suspicious cervical lymph nodes"
                },
                "Effect on the FNA size threshold": {
                    "Benign-leaning pattern": "Larger size needed before biopsy is considered",
                    "Suspicious pattern": "Lower threshold; biopsy considered at smaller sizes"
                }
            }
        },
        {
            "slug": "hot_vs_cold_nodule",
            "title": "Hot vs Cold Thyroid Nodules",
            "subtitle": "After a low TSH prompts a radionuclide scan, place each feature under the right nodule type",
            "categories": ["Hot (hyperfunctioning) nodule", "Cold (nonfunctioning) nodule"],
            "data": {
                "Radionuclide uptake in the nodule": {
                    "Hot (hyperfunctioning) nodule": "Focal increased uptake corresponding to the lesion",
                    "Cold (nonfunctioning) nodule": "Decreased uptake compared with surrounding thyroid tissue"
                },
                "Surrounding thyroid tissue": {
                    "Hot (hyperfunctioning) nodule": "Uptake suppressed in the rest of the gland",
                    "Cold (nonfunctioning) nodule": "Surrounding gland takes up tracer more avidly than the nodule"
                },
                "Malignancy risk": {
                    "Hot (hyperfunctioning) nodule": "Usually lower risk when the hot focus matches the lesion",
                    "Cold (nonfunctioning) nodule": "Not automatically malignant; risk comes from the ultrasound pattern"
                },
                "Role of fine-needle aspiration": {
                    "Hot (hyperfunctioning) nodule": "Usually not needed absent discordance or concerning features",
                    "Cold (nonfunctioning) nodule": "Indicated when size and ultrasound criteria are met"
                },
                "Main clinical priority": {
                    "Hot (hyperfunctioning) nodule": "Evaluate and treat thyroid hormone excess",
                    "Cold (nonfunctioning) nodule": "Ultrasound-based structural risk stratification of the nodule"
                }
            }
        },
        {
            "slug": "bethesda_categories",
            "title": "Bethesda Cytology: Result to Next Step",
            "subtitle": "Match each Bethesda result to its category number, its meaning, and where management heads next",
            "categories": ["Category number", "What the cytology shows", "Usual direction of next step"],
            "data": {
                "Nondiagnostic": {
                    "Category number": "Category I",
                    "What the cytology shows": "Sample inadequate for cytologic interpretation",
                    "Usual direction of next step": "Repeat sampling, usually with ultrasound guidance"
                },
                "Benign": {
                    "Category number": "Category II",
                    "What the cytology shows": "Benign follicular nodule pattern with no atypia",
                    "Usual direction of next step": "Clinical and ultrasound follow-up rather than surgery"
                },
                "Atypia of undetermined significance (AUS)": {
                    "Category number": "Category III",
                    "What the cytology shows": "Atypical cells falling short of a neoplasm diagnosis",
                    "Usual direction of next step": "Repeat sampling or molecular testing to refine risk"
                },
                "Follicular neoplasm / suspicious for follicular neoplasm (FLUS)": {
                    "Category number": "Category IV",
                    "What the cytology shows": "Follicular-pattern lesion that cytology cannot resolve",
                    "Usual direction of next step": "Molecular testing or diagnostic lobectomy to assess invasion"
                },
                "Suspicious for malignancy": {
                    "Category number": "Category V",
                    "What the cytology shows": "Features worrisome for but not diagnostic of cancer",
                    "Usual direction of next step": "Surgical evaluation, with extent guided by overall risk"
                },
                "Malignant": {
                    "Category number": "Category VI",
                    "What the cytology shows": "Cytology diagnostic of thyroid malignancy",
                    "Usual direction of next step": "Oncologic management of the diagnosed cancer"
                }
            }
        },
        {
            "slug": "thyroid_cancer_patterns",
            "title": "How the Thyroid Cancers Announce Themselves",
            "subtitle": "Match each thyroid cancer to its defining feature, its behavior, and the clue that points to it",
            "categories": ["Cell of origin or defining feature", "Characteristic spread or behavior", "Clue that points to it"],
            "data": {
                "Papillary thyroid carcinoma": {
                    "Cell of origin or defining feature": "Follicular epithelium; commonly presents as a thyroid nodule",
                    "Characteristic spread or behavior": "Spreads to cervical lymph nodes",
                    "Clue that points to it": "Suspicious cervical node with microcalcifications and cystic change"
                },
                "Follicular thyroid carcinoma": {
                    "Cell of origin or defining feature": "Defined by capsular and/or vascular invasion",
                    "Characteristic spread or behavior": "Hematogenous spread, especially to lung and bone",
                    "Clue that points to it": "Follicular-neoplasm cytology that cytology alone cannot settle"
                },
                "Medullary thyroid carcinoma": {
                    "Cell of origin or defining feature": "Arises from parafollicular C cells",
                    "Characteristic spread or behavior": "May be sporadic or MEN2/RET-associated",
                    "Clue that points to it": "Calcitonin production plus family history of pheochromocytoma"
                },
                "Anaplastic thyroid carcinoma": {
                    "Cell of origin or defining feature": "Highly aggressive undifferentiated thyroid malignancy",
                    "Characteristic spread or behavior": "Local invasion of neck structures with poor prognosis",
                    "Clue that points to it": "Rapid neck enlargement with hoarseness, dysphagia, and dyspnea"
                }
            }
        }
    ]
}
