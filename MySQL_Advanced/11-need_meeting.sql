-- creates a view listing students with score < 80 and no recent meeting

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
  AND (
      last_meeting IS NULL
      OR last_meeting < CURDATE() - INTERVAL 1 MONTH
  );
