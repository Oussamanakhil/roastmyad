CREATE TABLE roasts (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at timestamptz DEFAULT now(),
  caption text,
  transcript text,
  roast_text text,
  attention_score float,
  emotion_score float,
  clarity_score float,
  roastiq_score float,
  tags text[]
);
