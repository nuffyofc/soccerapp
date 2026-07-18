-- Roster update: Antoine Griezmann -> Lamine Yamal
-- Run in Supabase SQL Editor. The app also self-heals missing player rows
-- on load, but this keeps the table tidy immediately and removes
-- Griezmann's now-orphaned vote count instead of leaving it to rot.

insert into player_votes (id, votes) values ('yamal', 0)
on conflict (id) do nothing;

delete from player_votes where id = 'griezmann';
