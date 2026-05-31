/**
 * Kohra — a dark theme built on rules, not taste.
 *
 * Every token belongs to a bucket. Inside a bucket, lightness (L) and
 * chroma (C) are locked in OKLCH; only hue is free to move. Tokens of the
 * same role read as siblings because they are siblings in perceptual space.
 *
 * This file exists to be looked at: it touches every syntax bucket the
 * theme defines. Open it with Kohra active and the system is the picture.
 */

export type Bucket =
  | "syntax-primary"
  | "syntax-muted"
  | "comment"
  | "accent-primary"
  | "diagnostic";

interface Coord {
  l: number; // lightness, 0 to 1
  c: number; // chroma, 0 is grey
  h: number; // hue, in degrees
}

/** Locked (L, C) per bucket. Only the hue changes between siblings. */
const BUCKETS: Record<Bucket, Pick<Coord, "l" | "c">> = {
  "syntax-primary": { l: 0.78, c: 0.075 },
  "syntax-muted": { l: 0.62, c: 0.04 },
  comment: { l: 0.5, c: 0.012 },
  "accent-primary": { l: 0.78, c: 0.075 },
  diagnostic: { l: 0.65, c: 0.13 }, // the one window allowed to glow
};

const CHROMA_CEILING = 0.075;
const NEUTRAL_HUE = 240;

/** Conform a hue to its bucket and return an OKLCH string a theme can use. */
export function tokenColor(bucket: Bucket, hue = NEUTRAL_HUE): string {
  const { l, c } = BUCKETS[bucket];
  if (bucket !== "diagnostic" && c > CHROMA_CEILING) {
    throw new Error(`${bucket} breaks the chroma ceiling at ${c}`);
  }
  return `oklch(${l} ${c} ${hue})`;
}

// TODO: a light variant would be a second pass through every coordinate.
const keyword = tokenColor("syntax-primary", 264);
const string = tokenColor("syntax-muted", 146);
const error = tokenColor("diagnostic", 25);

console.log({ keyword, string, error, fog: tokenColor("comment") });
