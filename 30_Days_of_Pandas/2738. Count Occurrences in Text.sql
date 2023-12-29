(SELECT 'bull' AS word, COUNT(content) AS count FROM Files
WHERE content REGEXP ' \\bbull ')
UNION
(SELECT 'bear' AS word, COUNT(content) AS count FROM Files
WHERE content REGEXP ' \\bbear ')