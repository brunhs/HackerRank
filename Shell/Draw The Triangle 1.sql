DECLARE @var int
SELECT @var = 20
WHILE @var > 0
BEGIN
PRINT REPLICATE('* ', @var)
SET @var = @var - 1
END