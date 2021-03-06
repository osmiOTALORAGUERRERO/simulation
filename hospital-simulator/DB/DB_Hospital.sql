-- MySQL Script generated by MySQL Workbench
-- Sun Nov 22 16:21:53 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema hospital_simulator
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `hospital_simulator` ;

-- -----------------------------------------------------
-- Schema hospital_simulator
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hospital_simulator` DEFAULT CHARACTER SET utf8 ;
USE `hospital_simulator` ;

-- -----------------------------------------------------
-- Table `hospital_simulator`.`pacientes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`pacientes` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`pacientes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `tiempoTotal` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hospital_simulator`.`enfermeras`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`enfermeras` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`enfermeras` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hospital_simulator`.`doctores_urgencias`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`doctores_urgencias` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`doctores_urgencias` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hospital_simulator`.`registros_e`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`registros_e` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`registros_e` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `idEnfermera` INT NULL,
  `idPaciente` INT NULL,
  `tiempoAtencion` INT NULL,
  `tiempoAleatorio` FLOAT NULL,
  `diagnastico` ENUM('C') NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_e`
    FOREIGN KEY (`idEnfermera`)
    REFERENCES `hospital_simulator`.`enfermeras` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ep`
    FOREIGN KEY (`idPaciente`)
    REFERENCES `hospital_simulator`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_e_idx` ON `hospital_simulator`.`registros_e` (`idEnfermera` ASC) VISIBLE;

CREATE INDEX `fk_ep_idx` ON `hospital_simulator`.`registros_e` (`idPaciente` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `hospital_simulator`.`registros_du`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`registros_du` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`registros_du` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `idDoctorUrgencia` INT NULL,
  `idPaciente` INT NULL,
  `tiempoAtencion` INT NULL,
  `tiempoAleatorio` FLOAT NULL,
  `diagnostico` ENUM('SR', 'E') NULL DEFAULT NULL,
  `proceso` ENUM('1', '2') NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_du`
    FOREIGN KEY (`idDoctorUrgencia`)
    REFERENCES `hospital_simulator`.`doctores_urgencias` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pdu`
    FOREIGN KEY (`idPaciente`)
    REFERENCES `hospital_simulator`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_du_idx` ON `hospital_simulator`.`registros_du` (`idDoctorUrgencia` ASC) VISIBLE;

CREATE INDEX `fk_pdu_idx` ON `hospital_simulator`.`registros_du` (`idPaciente` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `hospital_simulator`.`radiografia`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`radiografia` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`radiografia` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT 'Radiografia',
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hospital_simulator`.`registros_r`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`registros_r` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`registros_r` (
  `id` INT NOT NULL,
  `idRadiografia` INT NULL,
  `idPaciente` INT NULL,
  `tiempoAtencion` INT NULL,
  `tiempoAleatorio` FLOAT NULL,
  `diagnostico` ENUM('DU') NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_r`
    FOREIGN KEY (`idRadiografia`)
    REFERENCES `hospital_simulator`.`radiografia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pr`
    FOREIGN KEY (`idPaciente`)
    REFERENCES `hospital_simulator`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_r_idx` ON `hospital_simulator`.`registros_r` (`idRadiografia` ASC) VISIBLE;

CREATE INDEX `fk_pr_idx` ON `hospital_simulator`.`registros_r` (`idPaciente` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `hospital_simulator`.`sala_radiografia`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`sala_radiografia` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`sala_radiografia` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT 'Sala Radiografia',
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hospital_simulator`.`registros_sr`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`registros_sr` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`registros_sr` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `idSalaRadiografia` INT NULL,
  `idPaciente` INT NULL,
  `tiempoEspera` INT NULL,
  `tiempoAleatorio` FLOAT NULL,
  `diagnostico` ENUM('R') NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_sr`
    FOREIGN KEY (`idSalaRadiografia`)
    REFERENCES `hospital_simulator`.`sala_radiografia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_psr`
    FOREIGN KEY (`idPaciente`)
    REFERENCES `hospital_simulator`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_psr_idx` ON `hospital_simulator`.`registros_sr` (`idPaciente` ASC) VISIBLE;

CREATE INDEX `fk_sr_idx` ON `hospital_simulator`.`registros_sr` (`idSalaRadiografia` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `hospital_simulator`.`doctores_admision`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`doctores_admision` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`doctores_admision` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hospital_simulator`.`registros_da`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`registros_da` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`registros_da` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `idDoctorAdmision` INT NULL,
  `idPaciente` INT NULL,
  `tiempoAtencion` INT NULL,
  `tiempoAleatorio` FLOAT NULL,
  `clasificacion` ENUM('G', 'MG', 'L') NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_da`
    FOREIGN KEY (`idDoctorAdmision`)
    REFERENCES `hospital_simulator`.`doctores_admision` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pda`
    FOREIGN KEY (`idPaciente`)
    REFERENCES `hospital_simulator`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_da_idx` ON `hospital_simulator`.`registros_da` (`idDoctorAdmision` ASC) VISIBLE;

CREATE INDEX `fk_pda_idx` ON `hospital_simulator`.`registros_da` (`idPaciente` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `hospital_simulator`.`hospital_ingreso`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`hospital_ingreso` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`hospital_ingreso` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT 'Ingreso',
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hospital_simulator`.`registros_hi`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`registros_hi` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`registros_hi` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `idPaciente` INT NULL,
  `idHospitalIngreso` INT NULL,
  `llegadaMin` INT NULL,
  `llegadaAleatorio` FLOAT NULL,
  `diagnostico` ENUM('DA') NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_hi`
    FOREIGN KEY (`idHospitalIngreso`)
    REFERENCES `hospital_simulator`.`hospital_ingreso` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_phi`
    FOREIGN KEY (`idPaciente`)
    REFERENCES `hospital_simulator`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_hi_idx` ON `hospital_simulator`.`registros_hi` (`idHospitalIngreso` ASC) VISIBLE;

CREATE INDEX `fk_phi_idx` ON `hospital_simulator`.`registros_hi` (`idPaciente` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `hospital_simulator`.`simulacion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hospital_simulator`.`simulacion` ;

CREATE TABLE IF NOT EXISTS `hospital_simulator`.`simulacion` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `min` INT NULL,
  `idRegistroDA` INT NULL,
  `idRegistroDU` INT NULL,
  `idRegistroE` INT NULL,
  `idRegistroR` INT NULL,
  `idRegistroSR` INT NULL,
  `idRegistroI` INT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_re`
    FOREIGN KEY (`idRegistroE`)
    REFERENCES `hospital_simulator`.`registros_e` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_rdu`
    FOREIGN KEY (`idRegistroDU`)
    REFERENCES `hospital_simulator`.`registros_du` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_rr`
    FOREIGN KEY (`idRegistroR`)
    REFERENCES `hospital_simulator`.`registros_r` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_rsr`
    FOREIGN KEY (`idRegistroSR`)
    REFERENCES `hospital_simulator`.`registros_sr` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_rda`
    FOREIGN KEY (`idRegistroDA`)
    REFERENCES `hospital_simulator`.`registros_da` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `jk_rhi`
    FOREIGN KEY (`idRegistroI`)
    REFERENCES `hospital_simulator`.`registros_hi` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_re_idx` ON `hospital_simulator`.`simulacion` (`idRegistroE` ASC) VISIBLE;

CREATE INDEX `fk_rdu_idx` ON `hospital_simulator`.`simulacion` (`idRegistroDU` ASC) VISIBLE;

CREATE INDEX `fk_rr_idx` ON `hospital_simulator`.`simulacion` (`idRegistroR` ASC) VISIBLE;

CREATE INDEX `fk_rsr_idx` ON `hospital_simulator`.`simulacion` (`idRegistroSR` ASC) VISIBLE;

CREATE INDEX `fk_rda_idx` ON `hospital_simulator`.`simulacion` (`idRegistroDA` ASC) VISIBLE;

CREATE INDEX `jk_rhi_idx` ON `hospital_simulator`.`simulacion` (`idRegistroI` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
