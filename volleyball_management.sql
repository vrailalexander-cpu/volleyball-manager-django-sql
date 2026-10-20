CREATE DATABASE IF NOT EXISTS volleyball_management
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
    
USE volleyball_management;

CREATE TABLE coaches (
    coach_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100) UNIQUE
);


CREATE TABLE players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    position ENUM(
        "Зв'язуючий",
        'Нападник',
        'Догравальник',
        'Центральний блокуючий',
        'Ліберо'
    ) NOT NULL,
    jersey_number INT NOT NULL,
    CONSTRAINT chk_jersey_number
        CHECK (jersey_number BETWEEN 1 AND 99)
) CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE TABLE teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL UNIQUE,
    coach_id INT,
    category VARCHAR(50),
    FOREIGN KEY (coach_id)
        REFERENCES coaches(coach_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

CREATE TABLE team_players (
    team_player_id INT AUTO_INCREMENT PRIMARY KEY,
    team_id INT NOT NULL,
    player_id INT NOT NULL,
    joined_at DATE NOT NULL,
    left_at DATE,
    FOREIGN KEY (team_id)
        REFERENCES teams(team_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (player_id)
        REFERENCES players(player_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT chk_membership_dates
        CHECK (left_at IS NULL OR left_at >= joined_at),
    UNIQUE (team_id, player_id, joined_at)
);

CREATE TABLE trainings (
    training_id INT AUTO_INCREMENT PRIMARY KEY,
    team_id INT NOT NULL,
    coach_id INT,
    training_datetime DATETIME NOT NULL,
    duration_minutes INT NOT NULL DEFAULT 90,
    location VARCHAR(150) NOT NULL,
    notes TEXT,
    FOREIGN KEY (team_id)
        REFERENCES teams(team_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (coach_id)
        REFERENCES coaches(coach_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    CONSTRAINT chk_training_duration
        CHECK (duration_minutes > 0)
);


CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    training_id INT NOT NULL,
    player_id INT NOT NULL,

    status ENUM(
        'Присутній',
        'Відсутній',
        'Запізнюється',
        'Виправданий'
    ) NOT NULL DEFAULT 'Присутній',

    comment VARCHAR(255),

    FOREIGN KEY (training_id)
        REFERENCES trainings(training_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (player_id)
        REFERENCES players(player_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    UNIQUE (training_id, player_id)
) CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE TABLE competitions (
    competition_id INT AUTO_INCREMENT PRIMARY KEY,
    competition_name VARCHAR(150) NOT NULL,
    location VARCHAR(150),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    competition_type VARCHAR(50),
    CONSTRAINT chk_competition_dates
        CHECK (end_date >= start_date)
);


CREATE TABLE matches (
    match_id INT AUTO_INCREMENT PRIMARY KEY,
    competition_id INT NOT NULL,
    home_team_id INT NOT NULL,
    away_team_id INT NOT NULL,
    match_datetime DATETIME NOT NULL,
    home_score INT NOT NULL DEFAULT 0,
    away_score INT NOT NULL DEFAULT 0,

    match_status ENUM(
        'Запланований',
        'Завершений',
        'Скасований'
    ) NOT NULL DEFAULT 'Запланований',

    FOREIGN KEY (competition_id)
        REFERENCES competitions(competition_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (home_team_id)
        REFERENCES teams(team_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    FOREIGN KEY (away_team_id)
        REFERENCES teams(team_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT chk_home_score
        CHECK (home_score >= 0),

    CONSTRAINT chk_away_score
        CHECK (away_score >= 0)

) CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

INSERT INTO coaches (first_name, last_name, phone, email)
VALUES
('Олександр', 'Петренко', '+380501112233', 'coach1@example.com'),
('Ірина', 'Коваленко', '+380671234567', 'coach2@example.com');
 
 
INSERT INTO players (first_name, last_name, birth_date, position, jersey_number)
VALUES
('Андрій', 'Шевченко', '2003-04-15', "Зв'язуючий", 7),
('Максим', 'Бондаренко', '2002-08-20', 'Догравальник', 10),
('Дмитро', 'Мельник', '2004-01-12', 'Ліберо', 16);

INSERT INTO teams (team_name, coach_id, category)
VALUES
('ВК Орли', 1, 'Доросла'),
('ВК Блискавка', 2, 'Молодіжна');

INSERT INTO team_players (team_id, player_id, joined_at)
VALUES
(1, 1, '2026-01-10'),
(2, 3, '2026-03-12');

INSERT INTO trainings (team_id, coach_id, training_datetime, duration_minutes, location, notes)
VALUES
(1, 1, '2026-10-15 17:00:00', 90, 'Спортивний зал №1', 'Техніка подачі та прийому'),
(2, 2, '2026-10-16 16:00:00', 120, 'Спортивний зал №2', 'Тактична підготовка');
 
INSERT INTO attendance (training_id, player_id, status)
VALUES
(1, 1, 'Присутній'),
(2, 3, 'Запізнюється');

INSERT INTO competitions (competition_name, location, start_date, end_date, competition_type)
VALUES
('Кубок міста з волейболу', 'Львів', '2026-11-01', '2026-11-07', 'Кубок'),
('Чемпіонат області', 'Львівська область', '2026-12-01', '2026-12-15', 'Чемпіонат');

INSERT INTO matches (competition_id, home_team_id, away_team_id, match_datetime, home_score, away_score, match_status)
VALUES
(1, 1, 2, '2026-11-02 18:00:00', 3, 1, 'Завершений'),
(2, 2, 1, '2026-12-05 17:00:00', 0, 0, 'Запланований');