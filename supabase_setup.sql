-- ============================================================
-- PickYourGOAT — real vote database setup (Supabase / Postgres)
-- ============================================================
-- Run this whole file once in your Supabase project's SQL Editor
-- (Dashboard > SQL Editor > New query > paste this in > Run).
--
-- Design: we only track a running total vote count PER PLAYER
-- (not per matchup pair). Simpler schema, fewer writes, easy to
-- stay under the free tier.
-- ============================================================

-- 1. Table: one row per player, one counter.
create table if not exists player_votes (
  id    text primary key,
  votes bigint not null default 0
);

-- 2. Seed the current 20-player roster at 0 votes.
--    (If you add/remove players later, the app will auto-seed any
--    missing IDs on load — you don't need to edit this file again.)
insert into player_votes (id, votes) values
  ('messi', 0), ('dibu', 0), ('julian', 0), ('deniro', 0),
  ('mbappe', 0), ('griezmann', 0), ('tchouameni', 0), ('dembele', 0),
  ('bellingham', 0), ('kane', 0), ('foden', 0), ('saka', 0),
  ('vinicius', 0), ('rodrygo', 0), ('raphinha', 0), ('casemiro', 0),
  ('ronaldo', 0), ('bfernandes', 0), ('leao', 0), ('cancelo', 0)
on conflict (id) do nothing;

-- 3. Lock the table down: anyone can READ counts, nobody can write
--    to it directly. All writes go through the increment_votes()
--    function below, which is the only path that can change data.
alter table player_votes enable row level security;

drop policy if exists "public read" on player_votes;
create policy "public read" on player_votes
  for select using (true);

revoke insert, update, delete on player_votes from anon, authenticated;
grant select on player_votes to anon, authenticated;

-- 4. Batched increment function. The app buffers votes in the
--    browser and sends one call like:
--      { "messi": 3, "ronaldo": 1 }
--    instead of one network request per tap — this is what keeps
--    request volume low on the free tier.
create or replace function increment_votes(deltas jsonb)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  player_id text;
  delta_val jsonb;
begin
  for player_id, delta_val in select * from jsonb_each(deltas) loop
    update player_votes
      set votes = votes + (delta_val::text)::bigint
      where id = player_id;
  end loop;
end;
$$;

grant execute on function increment_votes(jsonb) to anon, authenticated;

-- ============================================================
-- Done. Next: Project Settings > API, copy the "Project URL" and
-- "anon public" key into SUPABASE_URL / SUPABASE_ANON_KEY near the
-- top of the <script> in demo-soccer.html.
-- ============================================================
