/*
PGSQL Backup
Source Server Version: 9.4.0
Source Database: dbtest
Date: 2018/5/25 21:36:44
*/


-- ----------------------------
--  Sequence definition for "public"."django_migrations_id_seq"
-- ----------------------------
DROP SEQUENCE "public"."django_migrations_id_seq";
CREATE SEQUENCE "public"."django_migrations_id_seq"
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 1
 CACHE 1;;

-- ----------------------------
--  Table structure for "public"."django_migrations"
-- ----------------------------
DROP TABLE "public"."django_migrations";
CREATE TABLE "public"."django_migrations" (
"id" int4 DEFAULT nextval('django_migrations_id_seq'::regclass) NOT NULL,
"app" varchar(255) COLLATE "default" NOT NULL,
"name" varchar(255) COLLATE "default" NOT NULL,
"applied" timestamptz(6) NOT NULL,
PRIMARY KEY ("id")
)
WITH (OIDS=FALSE)
;;

-- ----------------------------
--  Table structure for "public"."sale_order"
-- ----------------------------
DROP TABLE "public"."sale_order";
CREATE TABLE "public"."sale_order" (
"id" int4 NOT NULL,
"name" varchar(255) COLLATE "default" NOT NULL,
"number" int4,
"sale_type_id" int4,
PRIMARY KEY ("id")
)
WITH (OIDS=FALSE)
;;

-- ----------------------------
--  Table structure for "public"."sale_order_line"
-- ----------------------------
DROP TABLE "public"."sale_order_line";
CREATE TABLE "public"."sale_order_line" (
"id" int4 NOT NULL,
"order_id" int4 NOT NULL,
"price" numeric(10,2),
"note" varchar(255) COLLATE "default",
PRIMARY KEY ("id")
)
WITH (OIDS=FALSE)
;;

-- ----------------------------
--  Table structure for "public"."sale_type"
-- ----------------------------
DROP TABLE "public"."sale_type";
CREATE TABLE "public"."sale_type" (
"id" int4 NOT NULL,
"t_name" varchar(255) COLLATE "default",
PRIMARY KEY ("id")
)
WITH (OIDS=FALSE)
;;

-- ----------------------------
--  Records 
-- ----------------------------
INSERT INTO "public"."sale_order" VALUES ('1','order1','1001','1'); INSERT INTO "public"."sale_order" VALUES ('2','order2','1002','1'); INSERT INTO "public"."sale_order" VALUES ('3','order3','1003','2'); INSERT INTO "public"."sale_order" VALUES ('4','order4','1004','3');
INSERT INTO "public"."sale_order_line" VALUES ('1','1','10.25','画笔1'); INSERT INTO "public"."sale_order_line" VALUES ('2','1','15.25','杯子'); INSERT INTO "public"."sale_order_line" VALUES ('3','1','2.12','笔记本'); INSERT INTO "public"."sale_order_line" VALUES ('4','2','15.21','测试1'); INSERT INTO "public"."sale_order_line" VALUES ('5','2','12.22','测试2'); INSERT INTO "public"."sale_order_line" VALUES ('6','2','1.11','测试3'); INSERT INTO "public"."sale_order_line" VALUES ('7','2','21.22','测试4'); INSERT INTO "public"."sale_order_line" VALUES ('8','3','11.20','测试8'); INSERT INTO "public"."sale_order_line" VALUES ('9','3','15.11','测试9'); INSERT INTO "public"."sale_order_line" VALUES ('10','4','44.44','111'); INSERT INTO "public"."sale_order_line" VALUES ('11','4','15.11','222'); INSERT INTO "public"."sale_order_line" VALUES ('12','4','16.33','333');
INSERT INTO "public"."sale_type" VALUES ('1','电器类'); INSERT INTO "public"."sale_type" VALUES ('2','家具类'); INSERT INTO "public"."sale_type" VALUES ('3','食品类');
