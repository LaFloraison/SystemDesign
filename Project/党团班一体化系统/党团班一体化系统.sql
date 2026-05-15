/*
 Navicat MySQL Dump SQL

 Source Server         : link1
 Source Server Type    : MySQL
 Source Server Version : 80044 (8.0.44)
 Source Host           : localhost:3306
 Source Schema         : 党团班一体化系统

 Target Server Type    : MySQL
 Target Server Version : 80044 (8.0.44)
 File Encoding         : 65001

 Date: 08/05/2026 16:59:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 党团员档案
-- ----------------------------
DROP TABLE IF EXISTS `党团员档案`;
CREATE TABLE `党团员档案`  (
  `档案ID` int NOT NULL AUTO_INCREMENT,
  `用户ID` int NOT NULL,
  `政治身份` enum('群众','团员','预备党员','党员') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `入团时间` date NULL DEFAULT NULL,
  `入党时间` date NULL DEFAULT NULL,
  `转正时间` date NULL DEFAULT NULL,
  `介绍人姓名` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `组织关系状态` enum('正常','转出','转入') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '正常',
  PRIMARY KEY (`档案ID`) USING BTREE,
  UNIQUE INDEX `用户ID`(`用户ID` ASC) USING BTREE,
  CONSTRAINT `fk_党团员档案_用户_用户ID` FOREIGN KEY (`用户ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 党团员档案
-- ----------------------------

-- ----------------------------
-- Table structure for 党团资料上传记录
-- ----------------------------
DROP TABLE IF EXISTS `党团资料上传记录`;
CREATE TABLE `党团资料上传记录`  (
  `记录ID` int NOT NULL AUTO_INCREMENT,
  `用户ID` int NOT NULL,
  `资料名称` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `资料路径` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `上传时间` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `审核状态` enum('待审核','已通过','已驳回') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '待审核',
  `审核人ID` int NULL DEFAULT NULL,
  `审核时间` datetime NULL DEFAULT NULL,
  `审核意见` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  PRIMARY KEY (`记录ID`) USING BTREE,
  INDEX `用户ID`(`用户ID` ASC) USING BTREE,
  INDEX `审核人ID`(`审核人ID` ASC) USING BTREE,
  CONSTRAINT `fk_党团资料上传记录_用户_用户ID` FOREIGN KEY (`用户ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_党团资料上传记录_用户_审核人ID` FOREIGN KEY (`审核人ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 党团资料上传记录
-- ----------------------------

-- ----------------------------
-- Table structure for 公示
-- ----------------------------
DROP TABLE IF EXISTS `公示`;
CREATE TABLE `公示`  (
  `公示ID` int NOT NULL AUTO_INCREMENT,
  `标题` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `内容` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `发布人ID` int NOT NULL,
  `发布时间` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `材料收集开始时间` datetime NULL DEFAULT NULL,
  `材料收集截止时间` datetime NULL DEFAULT NULL,
  `是否需要提交材料` enum('是','否') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '否',
  `状态` enum('进行中','已结束') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '进行中',
  PRIMARY KEY (`公示ID`) USING BTREE,
  INDEX `发布人ID`(`发布人ID` ASC) USING BTREE,
  CONSTRAINT `fk_公示_用户_发布人ID` FOREIGN KEY (`发布人ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 公示
-- ----------------------------

-- ----------------------------
-- Table structure for 公示材料提交记录
-- ----------------------------
DROP TABLE IF EXISTS `公示材料提交记录`;
CREATE TABLE `公示材料提交记录`  (
  `提交ID` int NOT NULL AUTO_INCREMENT,
  `公示ID` int NOT NULL,
  `用户ID` int NOT NULL,
  `材料内容` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `材料附件路径` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `提交时间` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `审核状态` enum('待审核','已通过','已驳回') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '待审核',
  `审核人ID` int NULL DEFAULT NULL,
  `审核时间` datetime NULL DEFAULT NULL,
  `审核意见` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  PRIMARY KEY (`提交ID`) USING BTREE,
  UNIQUE INDEX `uk_publicity_user`(`公示ID` ASC, `用户ID` ASC) USING BTREE,
  INDEX `用户ID`(`用户ID` ASC) USING BTREE,
  INDEX `审核人ID`(`审核人ID` ASC) USING BTREE,
  CONSTRAINT `fk_公示材料提交记录_公示_公示ID` FOREIGN KEY (`公示ID`) REFERENCES `公示` (`公示ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_公示材料提交记录_用户_用户ID` FOREIGN KEY (`用户ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_公示材料提交记录_用户_审核人ID` FOREIGN KEY (`审核人ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 公示材料提交记录
-- ----------------------------

-- ----------------------------
-- Table structure for 成员变更记录
-- ----------------------------
DROP TABLE IF EXISTS `成员变更记录`;
CREATE TABLE `成员变更记录`  (
  `变更ID` int NOT NULL AUTO_INCREMENT,
  `用户ID` int NOT NULL,
  `操作人ID` int NOT NULL,
  `变更内容` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `变更时间` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `变更前数据` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `变更后数据` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`变更ID`) USING BTREE,
  INDEX `用户ID`(`用户ID` ASC) USING BTREE,
  INDEX `操作人ID`(`操作人ID` ASC) USING BTREE,
  CONSTRAINT `fk_成员变更记录_用户_用户ID` FOREIGN KEY (`用户ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_成员变更记录_用户_操作人ID` FOREIGN KEY (`操作人ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 成员变更记录
-- ----------------------------

-- ----------------------------
-- Table structure for 推优任务
-- ----------------------------
DROP TABLE IF EXISTS `推优任务`;
CREATE TABLE `推优任务`  (
  `任务ID` int NOT NULL AUTO_INCREMENT,
  `任务名称` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `发布人ID` int NOT NULL,
  `发布时间` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `报名截止时间` datetime NULL DEFAULT NULL,
  `投票开始时间` datetime NULL DEFAULT NULL,
  `投票结束时间` datetime NULL DEFAULT NULL,
  `状态` enum('报名中','投票中','已结束') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '报名中',
  PRIMARY KEY (`任务ID`) USING BTREE,
  INDEX `发布人ID`(`发布人ID` ASC) USING BTREE,
  CONSTRAINT `fk_推优任务_用户_发布人ID` FOREIGN KEY (`发布人ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 推优任务
-- ----------------------------

-- ----------------------------
-- Table structure for 推优投票记录
-- ----------------------------
DROP TABLE IF EXISTS `推优投票记录`;
CREATE TABLE `推优投票记录`  (
  `投票ID` int NOT NULL AUTO_INCREMENT,
  `任务ID` int NOT NULL,
  `投票人ID` int NOT NULL,
  `被投票人ID` int NOT NULL,
  `投票时间` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`投票ID`) USING BTREE,
  UNIQUE INDEX `uk_task_voter`(`任务ID` ASC, `投票人ID` ASC, `被投票人ID` ASC) USING BTREE,
  INDEX `投票人ID`(`投票人ID` ASC) USING BTREE,
  INDEX `被投票人ID`(`被投票人ID` ASC) USING BTREE,
  CONSTRAINT `fk_推优投票记录_推优任务_任务ID` FOREIGN KEY (`任务ID`) REFERENCES `推优任务` (`任务ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_推优投票记录_用户_投票人ID` FOREIGN KEY (`投票人ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_推优投票记录_用户_被投票人ID` FOREIGN KEY (`被投票人ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 推优投票记录
-- ----------------------------

-- ----------------------------
-- Table structure for 推优报名
-- ----------------------------
DROP TABLE IF EXISTS `推优报名`;
CREATE TABLE `推优报名`  (
  `报名ID` int NOT NULL AUTO_INCREMENT,
  `任务ID` int NOT NULL,
  `用户ID` int NOT NULL,
  `报名时间` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `审核状态` enum('待审核','已通过','已驳回') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '待审核',
  `审核意见` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  PRIMARY KEY (`报名ID`) USING BTREE,
  UNIQUE INDEX `uk_task_user`(`任务ID` ASC, `用户ID` ASC) USING BTREE,
  INDEX `用户ID`(`用户ID` ASC) USING BTREE,
  CONSTRAINT `fk_推优报名_推优任务_任务ID` FOREIGN KEY (`任务ID`) REFERENCES `推优任务` (`任务ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_推优报名_用户_用户ID` FOREIGN KEY (`用户ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 推优报名
-- ----------------------------

-- ----------------------------
-- Table structure for 活动
-- ----------------------------
DROP TABLE IF EXISTS `活动`;
CREATE TABLE `活动`  (
  `活动ID` int NOT NULL AUTO_INCREMENT,
  `活动名称` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `活动描述` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `活动时间` datetime NOT NULL,
  `活动地点` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `发布人ID` int NOT NULL,
  `发布时间` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `签到码` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `签到截止时间` datetime NULL DEFAULT NULL,
  `状态` enum('报名中','进行中','已结束') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '报名中',
  PRIMARY KEY (`活动ID`) USING BTREE,
  INDEX `发布人ID`(`发布人ID` ASC) USING BTREE,
  CONSTRAINT `fk_活动_用户_发布人ID` FOREIGN KEY (`发布人ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 活动
-- ----------------------------

-- ----------------------------
-- Table structure for 活动报名记录
-- ----------------------------
DROP TABLE IF EXISTS `活动报名记录`;
CREATE TABLE `活动报名记录`  (
  `报名ID` int NOT NULL AUTO_INCREMENT,
  `活动ID` int NOT NULL,
  `用户ID` int NOT NULL,
  `报名时间` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `报名状态` enum('已报名','已取消') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '已报名',
  PRIMARY KEY (`报名ID`) USING BTREE,
  UNIQUE INDEX `uk_activity_user`(`活动ID` ASC, `用户ID` ASC) USING BTREE,
  INDEX `用户ID`(`用户ID` ASC) USING BTREE,
  CONSTRAINT `fk_活动报名记录_活动_活动ID` FOREIGN KEY (`活动ID`) REFERENCES `活动` (`活动ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_活动报名记录_用户_用户ID` FOREIGN KEY (`用户ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 活动报名记录
-- ----------------------------

-- ----------------------------
-- Table structure for 活动签到记录
-- ----------------------------
DROP TABLE IF EXISTS `活动签到记录`;
CREATE TABLE `活动签到记录`  (
  `签到ID` int NOT NULL AUTO_INCREMENT,
  `活动ID` int NOT NULL,
  `用户ID` int NOT NULL,
  `签到时间` datetime NULL DEFAULT NULL,
  `签到状态` enum('已签到','未签到') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '未签到',
  PRIMARY KEY (`签到ID`) USING BTREE,
  UNIQUE INDEX `uk_activity_sign`(`活动ID` ASC, `用户ID` ASC) USING BTREE,
  INDEX `用户ID`(`用户ID` ASC) USING BTREE,
  CONSTRAINT `fk_活动签到记录_活动_活动ID` FOREIGN KEY (`活动ID`) REFERENCES `活动` (`活动ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_活动签到记录_用户_用户ID` FOREIGN KEY (`用户ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 活动签到记录
-- ----------------------------

-- ----------------------------
-- Table structure for 用户
-- ----------------------------
DROP TABLE IF EXISTS `用户`;
CREATE TABLE `用户`  (
  `用户ID` int NOT NULL AUTO_INCREMENT COMMENT '主键，自增',
  `学号` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '学生学号，唯一不重复',
  `姓名` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '用户姓名',
  `性别` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '性别',
  `班级` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '所属班级',
  `手机号` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '手机号，唯一',
  `政治面貌` enum('群众','团员','党员','预备党员') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '政治面貌，固定选项',
  `入学时间` date NULL DEFAULT NULL COMMENT '入学时间',
  `角色` enum('普通学生','班长','团支书') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '普通学生' COMMENT '用户角色，默认普通学生，支撑权限逻辑',
  PRIMARY KEY (`用户ID`) USING BTREE,
  UNIQUE INDEX `学号`(`学号` ASC) USING BTREE,
  UNIQUE INDEX `手机号`(`手机号` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '用户基础信息表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 用户
-- ----------------------------

-- ----------------------------
-- Table structure for 考勤任务
-- ----------------------------
DROP TABLE IF EXISTS `考勤任务`;
CREATE TABLE `考勤任务`  (
  `考勤ID` int NOT NULL AUTO_INCREMENT COMMENT '主键，自增',
  `考勤名称` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '考勤任务名称',
  `考勤时间` datetime NOT NULL COMMENT '考勤时间',
  `考勤地点` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '考勤地点',
  `用户ID` int NOT NULL COMMENT '创建人ID，关联用户表（班委）',
  PRIMARY KEY (`考勤ID`) USING BTREE,
  INDEX `用户ID`(`用户ID` ASC) USING BTREE,
  CONSTRAINT `fk_考勤任务_用户_用户ID` FOREIGN KEY (`用户ID`) REFERENCES `用户` (`用户ID`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '考勤任务表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 考勤任务
-- ----------------------------

-- ----------------------------
-- Table structure for 考勤记录
-- ----------------------------
DROP TABLE IF EXISTS `考勤记录`;
CREATE TABLE `考勤记录`  (
  `记录ID` int NOT NULL AUTO_INCREMENT,
  `考勤日期` date NOT NULL,
  `用户ID` int NOT NULL,
  `录入人ID` int NOT NULL,
  `考勤状态` enum('出勤','缺勤','请假') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `备注` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`记录ID`) USING BTREE,
  INDEX `用户ID`(`用户ID` ASC) USING BTREE,
  INDEX `录入人ID`(`录入人ID` ASC) USING BTREE,
  CONSTRAINT `fk_考勤记录_用户_用户ID` FOREIGN KEY (`用户ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_考勤记录_用户_录入人ID` FOREIGN KEY (`录入人ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 考勤记录
-- ----------------------------

-- ----------------------------
-- Table structure for 证明材料
-- ----------------------------
DROP TABLE IF EXISTS `证明材料`;
CREATE TABLE `证明材料`  (
  `材料ID` int NOT NULL AUTO_INCREMENT COMMENT '主键，自增',
  `用户ID` int NOT NULL COMMENT '上传用户ID，关联用户表',
  `材料名称` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '材料名称',
  `上传时间` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '上传时间',
  `材料路径` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '材料存储路径',
  `审核状态` enum('待审核','通过','驳回') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '待审核' COMMENT '审核状态，固定选项',
  PRIMARY KEY (`材料ID`) USING BTREE,
  INDEX `用户ID`(`用户ID` ASC) USING BTREE,
  CONSTRAINT `fk_证明材料_用户_用户ID` FOREIGN KEY (`用户ID`) REFERENCES `用户` (`用户ID`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '证明材料表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 证明材料
-- ----------------------------

-- ----------------------------
-- Table structure for 请假申请
-- ----------------------------
DROP TABLE IF EXISTS `请假申请`;
CREATE TABLE `请假申请`  (
  `申请ID` int NOT NULL AUTO_INCREMENT,
  `用户ID` int NOT NULL,
  `请假日期` date NOT NULL,
  `请假原因` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `申请时间` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `审核状态` enum('待审核','已通过','已驳回') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '待审核',
  `审核人ID` int NULL DEFAULT NULL,
  `审核意见` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`申请ID`) USING BTREE,
  INDEX `用户ID`(`用户ID` ASC) USING BTREE,
  INDEX `审核人ID`(`审核人ID` ASC) USING BTREE,
  CONSTRAINT `fk_请假申请_用户_用户ID` FOREIGN KEY (`用户ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_请假申请_用户_审核人ID` FOREIGN KEY (`审核人ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 请假申请
-- ----------------------------

-- ----------------------------
-- Table structure for 通知
-- ----------------------------
DROP TABLE IF EXISTS `通知`;
CREATE TABLE `通知`  (
  `通知ID` int NOT NULL AUTO_INCREMENT COMMENT '主键，自增',
  `标题` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '通知标题',
  `内容` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '通知内容',
  `发布时间` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '发布时间，默认当前时间',
  `截止时间` datetime NULL DEFAULT NULL COMMENT '通知截止时间',
  `状态` enum('未发布','已发布','已过期') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '已发布' COMMENT '通知状态',
  `用户ID` int NOT NULL COMMENT '发布人ID，关联用户表',
  PRIMARY KEY (`通知ID`) USING BTREE,
  INDEX `用户ID`(`用户ID` ASC) USING BTREE,
  CONSTRAINT `fk_通知_用户_用户ID` FOREIGN KEY (`用户ID`) REFERENCES `用户` (`用户ID`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '通知信息表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 通知
-- ----------------------------

-- ----------------------------
-- Table structure for 通知已读记录
-- ----------------------------
DROP TABLE IF EXISTS `通知已读记录`;
CREATE TABLE `通知已读记录`  (
  `记录ID` int NOT NULL AUTO_INCREMENT,
  `通知ID` int NOT NULL,
  `用户ID` int NOT NULL,
  `已读时间` datetime NULL DEFAULT NULL,
  `状态` enum('未读','已读') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '未读',
  PRIMARY KEY (`记录ID`) USING BTREE,
  UNIQUE INDEX `uk_notice_user`(`通知ID` ASC, `用户ID` ASC) USING BTREE,
  INDEX `用户ID`(`用户ID` ASC) USING BTREE,
  CONSTRAINT `fk_通知已读记录_通知_通知ID` FOREIGN KEY (`通知ID`) REFERENCES `通知` (`通知ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_通知已读记录_用户_用户ID` FOREIGN KEY (`用户ID`) REFERENCES `用户` (`用户ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 通知已读记录
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
