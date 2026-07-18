-- Roster update: Rafael Leão -> Neymar
-- Run in Supabase SQL Editor after the app has been redeployed with the
-- Neymar roster change (the app also self-heals missing player rows on
-- load, but this keeps the table tidy immediately and removes Leão's
-- now-orphaned vote count instead of leaving it to rot).

insert into player_votes (id, votes) values ('neymar', 0)
on conflict (id) do nothing;

delete from player_votes where id = 'leao';
