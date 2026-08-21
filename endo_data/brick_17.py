BRICK = {
    "brick_num": 17,
    "brick_title": "Endocrine Bone Disorders",
    "games": [
        {
            "slug": "thin_soft_growing_bone",
            "title": "Osteoporosis vs Osteomalacia vs Rickets",
            "subtitle": "Sort each feature under the bone-weakening disorder it belongs to",
            "categories": ["Core bone defect", "Who is affected", "Usual cause", "Classic clinical picture", "Typical laboratory pattern"],
            "data": {
                "Osteoporosis": {
                    "Core bone defect": "Resorption exceeds formation, so bone mass is lost (thin bone)",
                    "Who is affected": "Adults, especially postmenopausal women and older patients",
                    "Usual cause": "Aging, estrogen loss, diabetes, smoking, inactivity, GI surgery",
                    "Classic clinical picture": "Silent until a hip, wrist, or vertebral fracture; kyphosis with height loss",
                    "Typical laboratory pattern": "Calcium, phosphorus, and vitamin D all normal; diagnosed by DEXA T score"
                },
                "Osteomalacia": {
                    "Core bone defect": "Defective mineralization of existing bone matrix (soft bone)",
                    "Who is affected": "Adults with impaired vitamin D supply or activation",
                    "Usual cause": "Vitamin D deficiency; also liver or kidney disease, antiepileptics",
                    "Classic clinical picture": "Cryptic bone pain, muscle weakness, trouble walking, pseudofractures",
                    "Typical laboratory pattern": "Low vitamin D, low calcium and/or phosphate, high alkaline phosphatase"
                },
                "Rickets": {
                    "Core bone defect": "Growth-plate cartilage and bone enlarge because they fail to mineralize",
                    "Who is affected": "Children whose growth plates are still open",
                    "Usual cause": "Low intake or malabsorption of calcium, phosphorus, or vitamin D",
                    "Classic clinical picture": "Bowed legs, thickened wrists and ankles, rachitic rosary, delayed walking",
                    "Typical laboratory pattern": "Deficiency of calcium, phosphorus, or vitamin D depending on the cause"
                }
            }
        },
        {
            "slug": "hyperostotic_dysplasias",
            "title": "Hyperostotic Bone Diseases",
            "subtitle": "Match each feature to the disorder of excessive bone formation",
            "categories": ["Gene and inheritance", "Bone cell at fault", "Direction of the mutation", "Long bone imaging clue", "Laboratory and marrow findings", "Treatment approach"],
            "data": {
                "Craniodiaphyseal dysplasia": {
                    "Gene and inheritance": "SOST at 17q21.31, autosomal dominant",
                    "Bone cell at fault": "Osteoblasts, the cells that lay down bone",
                    "Direction of the mutation": "Upregulating mutation drives osteoblast hyperfunctioning",
                    "Long bone imaging clue": "Policeman's night stick configuration of the femurs",
                    "Laboratory and marrow findings": "Increased PTH and alkaline phosphatase levels",
                    "Treatment approach": "Symptom driven; no medical therapy reverses the hyperostosis"
                },
                "Craniometaphyseal dysplasia": {
                    "Gene and inheritance": "ANKH at 5p15.2, autosomal dominant",
                    "Bone cell at fault": "Osteocytic osteocytes, which coordinate remodeling",
                    "Direction of the mutation": "ANKH mutation disrupts osteocyte control of remodeling",
                    "Long bone imaging clue": "Erlenmeyer flask flaring of the distal femoral metaphyses",
                    "Laboratory and marrow findings": "No distinctive labs; diagnosis is clinical, radiographic, and by DNA",
                    "Treatment approach": "Symptom driven; risky surgery to decompress cranial foramina"
                },
                "Osteopetrosis": {
                    "Gene and inheritance": "Multiple genes; dominant or recessive depending on the kindred",
                    "Bone cell at fault": "Osteoclasts, the cells that resorb bone",
                    "Direction of the mutation": "Downregulating mutations cause osteoclast hypofunctioning",
                    "Long bone imaging clue": "Generalized dense bone that still fractures easily",
                    "Laboratory and marrow findings": "Marrow hypocellularity with compensatory extramedullary hematopoiesis",
                    "Treatment approach": "Bone marrow transplant, because osteoclasts are transplantable cells"
                }
            }
        },
        {
            "slug": "signal_transduction_gnas",
            "title": "Post-Receptor Signal Transduction and GNAS",
            "subtitle": "Match each concept or disorder to its definition, signaling role, and clinical correlate",
            "categories": ["What it is", "Role in signaling", "Clinical correlate"],
            "data": {
                "Post-receptor signal transduction": {
                    "What it is": "The internal biochemical events after a molecule binds a surface receptor",
                    "Role in signaling": "G proteins, second messengers, and protein kinases relay the signal inward",
                    "Clinical correlate": "Hormone-receptor binding alone is not enough to produce the hormone's effect"
                },
                "GNAS locus": {
                    "What it is": "A multimeric imprinted locus using alternative promoters and splicing",
                    "Role in signaling": "Serves as a second messenger for thyroid, PTH, FSH, LH, and GH signaling",
                    "Clinical correlate": "Mutations here underlie recognized endocrine bone disorders"
                },
                "Gs-alpha": {
                    "What it is": "The best-characterized GNAS transcript, alpha subunit of the stimulatory G protein",
                    "Role in signaling": "Couples the activated receptor to the stimulatory guanine nucleotide-binding protein",
                    "Clinical correlate": "Mutated in Albright hereditary osteodystrophy and McCune-Albright syndrome"
                },
                "Genomic imprinting": {
                    "What it is": "Epigenetic silencing of one allele based on which parent supplied it",
                    "Role in signaling": "Decides which parental GNAS allele is actually expressed in a tissue",
                    "Clinical correlate": "About 70 of the roughly 22,000 human genes are imprinted"
                },
                "Albright hereditary osteodystrophy": {
                    "What it is": "Pseudohypoparathyroidism type 1A caused by a Gs-alpha defect",
                    "Role in signaling": "Tissues cannot transduce the PTH signal, so urinary cyclic AMP barely rises",
                    "Clinical correlate": "Short stature, obesity, ectopic calcifications, hypocalcemia with high PTH"
                },
                "McCune-Albright syndrome": {
                    "What it is": "A second Gs-alpha GNAS disorder with skin, bone, and endocrine disease",
                    "Role in signaling": "Altered Gs-alpha drives overactivity of several hormone axes at once",
                    "Clinical correlate": "Hyperpigmented macules, polyostotic fibrous dysplasia, precocious puberty"
                }
            }
        },
        {
            "slug": "signature_bone_findings",
            "title": "Signature Findings in Endocrine Bone Disease",
            "subtitle": "Match each buzzword finding to where it is found, its disease, and its mechanism",
            "categories": ["Where it is found", "Disease it points to", "Mechanism behind it"],
            "data": {
                "Rachitic rosary": {
                    "Where it is found": "Bead-like enlargements felt along the costochondral junctions",
                    "Disease it points to": "Rickets",
                    "Mechanism behind it": "Unmineralized cartilage and bone pile up at growing junctions"
                },
                "Policeman's night stick femurs": {
                    "Where it is found": "Skeletal x-ray of the long bones, with craniofacial hyperostosis",
                    "Disease it points to": "Craniodiaphyseal dysplasia",
                    "Mechanism behind it": "Osteoblast hyperfunctioning from an upregulating SOST mutation"
                },
                "Erlenmeyer flask deformity": {
                    "Where it is found": "Broadened metaphyses of the distal femur in childhood",
                    "Disease it points to": "Craniometaphyseal dysplasia",
                    "Mechanism behind it": "Osteocytic osteocyte dysfunction from an ANKH mutation"
                },
                "T score of -2.5 or lower": {
                    "Where it is found": "Report of a dual-energy x-ray absorptiometry scan",
                    "Disease it points to": "Osteoporosis",
                    "Mechanism behind it": "Resorption outpacing formation leaves porous, fragile bone"
                },
                "Pseudofractures with high alkaline phosphatase": {
                    "Where it is found": "Adult with bone pain, weakness, and low vitamin D",
                    "Disease it points to": "Osteomalacia",
                    "Mechanism behind it": "Defective mineralization of matrix, usually from vitamin D deficiency"
                },
                "Emissary veins through the cranium": {
                    "Where it is found": "Skull of a patient with thickened cranial bones",
                    "Disease it points to": "Hyperostosis with intracranial hypertension",
                    "Mechanism behind it": "Shunt pathway bypassing foramina that obstruct venous egress"
                }
            }
        }
    ]
}
