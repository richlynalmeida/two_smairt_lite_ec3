--
UPDATE auth_user
SET first_name = 'Hetty (2SMAiRT Manager)',
    last_name  = 'King',
    email      = 'hetty.king@2smairt.com'
WHERE id = 1;
-- auth_user (MixinsModel)
INSERT INTO auth_user (id, "password", last_login, is_superuser, username, first_name, last_name, email,
                       is_staff, is_active, date_joined)
VALUES (1, 'pbkdf2_sha256$600000$PhW3jB0sXnWNHr4A3vlrf6$+rUCA50p5j5dtUAZSjaoyXcTT9okEJJKI2iE1tb6J7c=', NULL, TRUE,
        'hking', 'Hetty (2SMAiRT Manager)', 'King', 'hetty.king@2smairt.com', TRUE, TRUE, NOW()),
       (2, 'pbkdf2_sha256$600000$PhW3jB0sXnWNHr4A3vlrf6$+rUCA50p5j5dtUAZSjaoyXcTT9okEJJKI2iE1tb6J7c=', NULL, FALSE,
        'gpike', 'Gus (Construction Coordinator)', 'Pike', 'gus.pike@2smairt.com', TRUE, TRUE, NOW()),
       (3, 'pbkdf2_sha256$600000$PhW3jB0sXnWNHr4A3vlrf6$+rUCA50p5j5dtUAZSjaoyXcTT9okEJJKI2iE1tb6J7c=', NULL, FALSE,
        'jdale', 'Jasper (Design Engineer)', 'Dale', 'jasper.dale@2smairt.com', TRUE, TRUE, NOW()),
       (4, 'pbkdf2_sha256$600000$PhW3jB0sXnWNHr4A3vlrf6$+rUCA50p5j5dtUAZSjaoyXcTT9okEJJKI2iE1tb6J7c=', NULL, FALSE,
        'sstanley', 'Sara (Engineering Manager)', 'Stanley', 'sara.stanley@2smairt.com', TRUE, TRUE, NOW()),
       (5, 'pbkdf2_sha256$600000$PhW3jB0sXnWNHr4A3vlrf6$+rUCA50p5j5dtUAZSjaoyXcTT9okEJJKI2iE1tb6J7c=', NULL, FALSE,
        'rlynde', 'Rachel (Client Project Manager)', 'Lynde', 'rachel.lynde@2smairt.com', FALSE, TRUE, NOW()),
       (6, 'pbkdf2_sha256$600000$PhW3jB0sXnWNHr4A3vlrf6$+rUCA50p5j5dtUAZSjaoyXcTT9okEJJKI2iE1tb6J7c=', NULL, FALSE,
        'aking', 'Alex (Construction Manager)', 'King', 'alex.king@2smairt.com', TRUE, TRUE, NOW()),
       (7, 'pbkdf2_sha256$600000$PhW3jB0sXnWNHr4A3vlrf6$+rUCA50p5j5dtUAZSjaoyXcTT9okEJJKI2iE1tb6J7c=', NULL, FALSE,
        'mstacey', 'Muriel (Project Manager)', 'Stacey', 'muriel.stacey@2smairt.com', TRUE, TRUE, NOW()),
       (8, 'pbkdf2_sha256$600000$PhW3jB0sXnWNHr4A3vlrf6$+rUCA50p5j5dtUAZSjaoyXcTT9okEJJKI2iE1tb6J7c=', NULL, FALSE,
        'cpettibone', 'Clive (Commercial Manager)', 'Pettibone', 'clive.pettibone@2smairt.com', TRUE, TRUE, NOW()),
       (9, 'pbkdf2_sha256$600000$PhW3jB0sXnWNHr4A3vlrf6$+rUCA50p5j5dtUAZSjaoyXcTT9okEJJKI2iE1tb6J7c=', NULL, FALSE,
        'stremayne', 'Simon (Project Services Manager)', 'Tremayne', 'simon.tremayne@2smairt.com', TRUE, TRUE, NOW()),
       (10, 'pbkdf2_sha256$600000$PhW3jB0sXnWNHr4A3vlrf6$+rUCA50p5j5dtUAZSjaoyXcTT9okEJJKI2iE1tb6J7c=', NULL, FALSE,
        'fking', 'Felicity (Project Controls Manager)', 'King', 'felicity.king@2smairt.com', TRUE, TRUE,
        NOW()) ON CONFLICT (id) DO NOTHING;
SELECT setval('auth_user_id_seq', (SELECT MAX(id) FROM auth_user));

INSERT INTO project (
    created_at,
    updated_at,
    is_deleted,
    deleted_at,
    project_id,
    project_code,
    project_title,
    venue,
    "comments",
    is_active,
    start_date,
    finish_date
)
VALUES (
    now(),
    now(),
    'N',
    NULL,
    1,
    'BESS-A',
    'SA Power – BESS A',
    'South Australia',
    'Initial EC3 FinishLine / 2SMAiRT Lite demonstration project',
    'Y',
    DATE '2025-01-01',
    DATE '2026-06-30'
)
ON CONFLICT (project_id) DO NOTHING;

SELECT SETVAL(
    'project_project_id_seq',
    (SELECT MAX(project_id) FROM project)
);


INSERT INTO project_structure (
    created_at,
    updated_at,
    is_deleted,
    deleted_at,
    project_structure_id,
    structure_code,
    structure_title,
    structure_level,
    structure_role,
    "comments",
    is_active,
    sort_order,
    parent_project_structure_id,
    project_id
)
VALUES (
    now(),
    now(),
    'N',
    NULL,
    1,
    'BOP',
    'Balance of Plant',
    1,
    'SPATIAL',
    'Non-battery, non-PCS supporting works and systems',
    'Y',
    10,
    NULL,
    1
)
ON CONFLICT (project_structure_id) DO NOTHING;

SELECT SETVAL(
    'project_structure_project_structure_id_seq',
    (SELECT MAX(project_structure_id) from project_structure)
);



-- company_category
INSERT INTO company_category (company_category_id, company_category_code, company_category_title, "comments")
VALUES
--    (1, 'C', 'Customers', null, true, false, now(), now(), 1),
(1, 'C', 'Customers', null),
(2, 'L', 'Legal Services', null),
(3, 'F', 'Freight Services', null),
(4, 'S', 'Suppliers', null),
(5, 'Z', 'Placeholder Category', null),
(6, 'P', 'Professional Services', null),
(7, 'T', 'Construction', null) ON CONFLICT (company_category_id) DO NOTHING;
SELECT SETVAL('"company_category_company_category_id_seq"', (SELECT max(company_category_id) FROM "company_category"));
-- company
INSERT INTO company_item (company_item_id, company_item_code, company_item_title, email, business_phone, fax_number, address1, address2, zip_postal_code, city, state_province, country, web_page, "comments", company_category_id)
VALUES (1,'PLH','Placeholder Company','placeholder@company.com','111111111','111111111','ABC Drive',NULL,'XXX XXX','Calgary','AB','Canada','www.plh.com','None',5),
       (2,'ABC','ABC Claims Specialists','abc@company.com','111111111','111111111','ABC Drive',NULL,'XXX XXX','New York','NY','USA','www.abc.com','None',6),
       (3,'BCD','BCD Constructors','bcd@company.com','111111111','111111111','BCD Drive',NULL,'XXX XXX','Edmonton','AB','Canada','www.bcd.com','None',7),
       (4,'CDE','CDE Engineers','cde@company.com','1111111111','111111111','CDE Drive',NULL,'XXX XXX','Toronto','ON','Canada','www.cde.com','None',6),
       (5,'DEF','DEF Freight and Logistics','def@company.com','111111111','111111111','DEF Drive',NULL,'XXX XXX','Sydney','NSW','Australia','www.def.com','None',3),
       (6,'EFG','EFG Suppliers','efg@company.com','111111111','111111111','EFG Drive',NULL,'XXX XXX','Houston','TX','USA','www.efg.com','None',4),
       (7,'FGH','FGH Fabricators','fgh@company.com','111111111','111111111','FGH Drive',NULL,'XXX XXX','Charleston','SC','USA','www.fgh.com','None',7),
       (8,'GHI','GHI Legal','ghi@company.com','111111111','111111111','GHI Drive',NULL,'XXX XXX','Brisbane','QLD','Australia','www.ghi.com','None',2),
       (9,'HIJ','HIJ Rentals','hij@company.com','111111111','111111111','HIJ Drive',NULL,'XXX XXX','Frederick','MD','USA','www.hij.com','None',7),
       (10,'XYZ','XYZ Mining','xyz@company.com','111111111','111111111','XYZ Drive',NULL,'XXX XXX','Pilbara','WA','Australia','www.xyz.com','None',1),
       (11,'WXY','WXY Oil Field Services','wxy@company.com','111111111','111111111','WXY Drive',NULL,'XXX XXX','Manama','MA','Oman','www.wxy.com','None',1)
       ON CONFLICT (company_item_id) DO NOTHING;
SELECT SETVAL('"company_item_company_item_id_seq"',
                (SELECT max(company_item_id)
                 FROM "company_item"));

