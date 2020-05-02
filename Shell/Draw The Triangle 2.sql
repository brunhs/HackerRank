DECLARE @var int
SELECT @var = 0
WHILE @var <= 20
BEGIN
PRINT REPLICATE('* ', @var)
SET @var = @var + 1
END