CREATE OR REPLACE FUNCTION GetGroupItems(channelid integer)
  RETURNS TABLE(id integer, name varchar, info text)
AS $$
DECLARE

BEGIN
    RETURN QUERY SELECT I.id, I.name, I.info
    FROM Item I
    INNER JOIN ChannelItem CI
    ON CI.item_id = I.id
    AND CI.channel_id = channelid;

END;$$

LANGUAGE 'plpgsql';
