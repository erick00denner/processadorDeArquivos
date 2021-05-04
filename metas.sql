CREATE TABLE `dim_meta` (
	`metaID` INT NOT NULL AUTO_INCREMENT,
	`metaNome` TEXT NOT NULL,
	`inicioVigencia` DATE NOT NULL,
	`fimVigencia` DATE NOT NULL,
	`fk_unidadeMedida` int NOT NULL,
	`metaPositiva` bool NOT NULL,
	PRIMARY KEY (`metaID`)
);

CREATE TABLE `ft_lancamentoMetas` (
	`lancamentoID` int NOT NULL AUTO_INCREMENT,
	`fk_postoAgencia` int NOT NULL,
	`fk_metaID` int NOT NULL,
	`dataVigencia` DATE NOT NULL,
	`valorLancamento` FLOAT NOT NULL,
	PRIMARY KEY (`lancamentoID`)
);

CREATE TABLE `dim_agencia` (
	`postoAgencia` int NOT NULL,
	`nomeAgencia` TEXT NOT NULL,
	PRIMARY KEY (`postoAgencia`)
);

CREATE TABLE `dim_unidadesMedida` (
	`unidadeID` int NOT NULL AUTO_INCREMENT,
	`unidadeNome` TEXT NOT NULL,
	PRIMARY KEY (`unidadeID`)
);

CREATE TABLE `ft_metaAgencia` (
	`metaAgencia` int NOT NULL AUTO_INCREMENT,
	`fk_metaID` int NOT NULL,
	`fk_agencia` int NOT NULL,
	`valorMeta` FLOAT NOT NULL,
	PRIMARY KEY (`metaAgencia`)
);

ALTER TABLE `dim_meta` ADD CONSTRAINT `dim_meta_fk0` FOREIGN KEY (`fk_unidadeMedida`) REFERENCES `dim_unidadesMedida`(`unidadeID`);

ALTER TABLE `ft_lancamentoMetas` ADD CONSTRAINT `ft_lancamentoMetas_fk0` FOREIGN KEY (`fk_postoAgencia`) REFERENCES `dim_agencia`(`postoAgencia`);

ALTER TABLE `ft_lancamentoMetas` ADD CONSTRAINT `ft_lancamentoMetas_fk1` FOREIGN KEY (`fk_metaID`) REFERENCES `dim_meta`(`metaID`);

ALTER TABLE `ft_metaAgencia` ADD CONSTRAINT `ft_metaAgencia_fk0` FOREIGN KEY (`fk_metaID`) REFERENCES `dim_meta`(`metaID`);

ALTER TABLE `ft_metaAgencia` ADD CONSTRAINT `ft_metaAgencia_fk1` FOREIGN KEY (`fk_agencia`) REFERENCES `dim_agencia`(`postoAgencia`);

