BRICK = {
    "brick_num": 13,
    "brick_title": "Differentiated Thyroid Cancers: Papillary and Follicular Thyroid Carcinoma",
    "games": [
        {
            "slug": "ptc_vs_ftc",
            "title": "Papillary vs Follicular Thyroid Carcinoma",
            "subtitle": "Sort each feature under the differentiated thyroid cancer it describes",
            "categories": ["How common", "Diagnostic clue", "Value of fine-needle aspiration", "Route of spread", "Typical metastatic site", "Molecular pattern"],
            "data": {
                "Papillary thyroid carcinoma": {
                    "How common": "The most common thyroid cancer overall",
                    "Diagnostic clue": "Nuclear phenotype: clearing, grooves, pseudoinclusions, psammoma bodies",
                    "Value of fine-needle aspiration": "Cytology alone can show the diagnostic nuclear features",
                    "Route of spread": "Lymphatic spread to cervical lymph nodes",
                    "Typical metastatic site": "Cervical nodes, even when the primary tumor is small",
                    "Molecular pattern": "MAPK-pathway pattern, including BRAF V600E and RET fusions"
                },
                "Follicular thyroid carcinoma": {
                    "How common": "Less common differentiated cancer of follicular pattern",
                    "Diagnostic clue": "Capsular and/or vascular invasion seen in tissue",
                    "Value of fine-needle aspiration": "Cytology says only 'follicular neoplasm'; invasion cannot be assessed",
                    "Route of spread": "Hematogenous, blood-borne spread",
                    "Typical metastatic site": "Bone and lung",
                    "Molecular pattern": "RAS-like pattern, including PAX8::PPAR-gamma fusion"
                }
            }
        },
        {
            "slug": "histology_clues",
            "title": "Microscopic Clues in Differentiated Thyroid Cancer",
            "subtitle": "Match each microscopic finding to what it looks like, what it establishes, and its pitfall",
            "categories": ["Microscopic appearance", "Diagnostic significance", "Pitfall to avoid"],
            "data": {
                "Nuclear clearing": {
                    "Microscopic appearance": "Optically clear, empty-looking 'Orphan Annie eye' nuclei",
                    "Diagnostic significance": "Core nuclear criterion for papillary thyroid carcinoma",
                    "Pitfall to avoid": "Waiting for true papillae; the nuclei carry the diagnosis"
                },
                "Nuclear grooves": {
                    "Microscopic appearance": "Longitudinal indentations folding the nuclear membrane",
                    "Diagnostic significance": "Supports papillary carcinoma alongside the other nuclear clues",
                    "Pitfall to avoid": "Calling follicular carcinoma; grooves are not its defining feature"
                },
                "Intranuclear pseudoinclusions": {
                    "Microscopic appearance": "Cytoplasm invaginating into the nucleus as a round inclusion",
                    "Diagnostic significance": "Strong cytologic clue to papillary carcinoma on aspiration",
                    "Pitfall to avoid": "Attributing them to autoimmune thyroiditis with Hurthle cell change"
                },
                "Psammoma bodies": {
                    "Microscopic appearance": "Laminated, concentrically calcified round bodies",
                    "Diagnostic significance": "Classic papillary carcinoma finding on histology",
                    "Pitfall to avoid": "Overlooking the matching punctate echogenic foci on ultrasound"
                },
                "Capsular invasion": {
                    "Microscopic appearance": "Tumor breaching the full thickness of the fibrous capsule",
                    "Diagnostic significance": "Establishes follicular carcinoma rather than follicular adenoma",
                    "Pitfall to avoid": "Trying to judge it on aspiration cytology, which cannot see the capsule"
                },
                "Vascular invasion": {
                    "Microscopic appearance": "Tumor plugs inside capsular or extracapsular blood vessels",
                    "Diagnostic significance": "Also establishes carcinoma and explains blood-borne spread",
                    "Pitfall to avoid": "Assuming a molecular result can substitute for seeing invasion"
                }
            }
        },
        {
            "slug": "molecular_patterns",
            "title": "Molecular Drivers and What They Really Tell You",
            "subtitle": "Match each molecular finding to the pattern it supports, its clinical use, and its limitation",
            "categories": ["Pattern it supports", "Clinical use", "Interpretation limit"],
            "data": {
                "BRAF V600E (MAPK-pathway pattern)": {
                    "Pattern it supports": "Papillary thyroid carcinoma biology",
                    "Clinical use": "Helps classify a nodule when cytology is indeterminate",
                    "Interpretation limit": "Does not replace the nuclear morphology that defines papillary carcinoma"
                },
                "RAS mutation (RAS-like pattern)": {
                    "Pattern it supports": "Follicular-pattern thyroid tumors",
                    "Clinical use": "Supports a follicular-pattern pathway on indeterminate cytology",
                    "Interpretation limit": "Cannot separate follicular adenoma from follicular carcinoma"
                },
                "PAX8::PPAR-gamma fusion": {
                    "Pattern it supports": "Follicular-pattern neoplasm pathway",
                    "Clinical use": "Adds support to a follicular-pattern classification",
                    "Interpretation limit": "Does not by itself prove capsular or vascular invasion"
                },
                "TERT promoter mutation": {
                    "Pattern it supports": "Aggressive behavior in differentiated thyroid cancer",
                    "Clinical use": "Raises risk concern and may affect management intensity",
                    "Interpretation limit": "A risk marker, not a first-pass diagnostic label"
                },
                "Somatic RET fusion": {
                    "Pattern it supports": "Papillary thyroid carcinoma arising from follicular cells",
                    "Clinical use": "Reinforces the papillary molecular pattern in the tumor",
                    "Interpretation limit": "Must not be read as an inherited cancer syndrome finding"
                },
                "Germline activating RET variant": {
                    "Pattern it supports": "MEN2-associated medullary thyroid carcinoma, a different lineage",
                    "Clinical use": "Drives family testing and prophylactic thyroid surgery decisions",
                    "Interpretation limit": "Same gene name as the papillary fusion, but different disease logic"
                }
            }
        },
        {
            "slug": "treatment_surveillance",
            "title": "Treatment and Surveillance of Differentiated Thyroid Cancer",
            "subtitle": "Match each tool to its role, the follicular-cell biology behind it, and its caveat",
            "categories": ["Role in care", "Biologic rationale", "Caveat"],
            "data": {
                "Surgery": {
                    "Role in care": "Usual main initial treatment for differentiated thyroid cancer",
                    "Biologic rationale": "Removes the tumor-bearing follicular tissue at the source",
                    "Caveat": "Extent ranges from lobectomy to total thyroidectomy and is risk-adapted"
                },
                "Radioactive iodine": {
                    "Role in care": "Used selectively after surgery rather than in every patient",
                    "Biologic rationale": "Differentiated tumor cells may retain iodine-handling machinery",
                    "Caveat": "Most useful only when residual or metastatic disease is iodine-avid"
                },
                "Levothyroxine for TSH suppression": {
                    "Role in care": "Lowers thyroid-stimulating hormone drive after treatment",
                    "Biologic rationale": "Differentiated tumor cells may still respond to TSH",
                    "Caveat": "Intensity of suppression is risk-adapted, not maximal for everyone"
                },
                "Thyroglobulin monitoring": {
                    "Role in care": "Serum tumor marker followed during surveillance",
                    "Biologic rationale": "Normal and differentiated malignant follicular cells both make thyroglobulin",
                    "Caveat": "Most informative once surgery or ablation has removed normal thyroid tissue"
                },
                "Anti-thyroglobulin antibodies": {
                    "Role in care": "Measured alongside every surveillance thyroglobulin level",
                    "Biologic rationale": "Antibodies against thyroglobulin distort the thyroglobulin assay",
                    "Caveat": "When positive, a low thyroglobulin cannot be taken as reassuring"
                },
                "Neck ultrasound": {
                    "Role in care": "Imaging arm of routine post-treatment follow-up",
                    "Biologic rationale": "Detects structural disease in the thyroid bed and cervical nodes",
                    "Caveat": "Anatomic, so it complements rather than replaces biochemical testing"
                }
            }
        }
    ]
}
