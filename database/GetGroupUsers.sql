CREATE OR REPLACE FUNCTION GetGroupUsers(channelid integer)
  RETURNS TABLE(id integer, name varchar, secondName varchar, isAdmin bit)
AS $$
DECLARE

BEGIN
    RETURN QUERY
    SELECT U.id, U.name, U.secondName, CU.isAdmin
    FROM Users U
    INNER JOIN ChannelUser CU
    ON CU.user_id = U.id
    AND CU.channel_id = channelid;

END;$$

LANGUAGE 'plpgsql';

