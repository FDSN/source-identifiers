
const fdsnPrefix = 'FDSN:';
const sep = '_';

const sidRegExString = '^FDSN:'              // Required prefix
                       +'([A-Z0-9]{1,8})'     // Required network: upper-alphanumeric
                       +'(_([-A-Z0-9]{1,8})'  // Optional non-empty station: upper-alphanumeric and dash
                       +'(_([-A-Z0-9]{0,8})'  // Optional possibly-empty location: upper-alphanumeric and dash
                       +'(_(([A-Z0-9]*)_([A-Z0-9]+)_([A-Z0-9]*))' // Optional channel with non-empty source: upper-alphanumeric
                       +')?)?)?$';
const sidRegEx = new RegExp(sidRegExString);

const tempNetRegEx = /^([XYZ0-9][A-Z0-9])([0-9]{4})$/;

const netRegEx = /^[A-Z0-9]{1,2}$/;
const staRegEx = /^[A-Z0-9]{1,5}$/;
const locRegEx = /^[A-Z0-9]{0,2}$/;
const chanRegEx = /^[A-Z0-9]{3}$/;

function validateNSLC(net, sta, loc, chan) {
  return netRegEx.test(net)
    && staRegEx.test(sta)
    && locRegEx.test(loc)
    && chanRegEx.test(chan);
}

function validateSid(sid) {
  return sidRegEx.test(sid);
}

function nslcToSid(net, sta, loc, chan) {
  if (! validateNSLC(net, sta, loc, chan)) {
    throw new Error(`Invalid NSLC.`);
  }
  let sid = `${fdsnPrefix}${net}${sep}${sta}${sep}${loc}${sep}${chan.split('').join(sep)}`;
  if (!validateSid(sid)) {
    throw new Error(`Resulting Source Id is invalid: ${sid}`);
  }
  return sid;
}

function parseSid(sid) {
  if ( ! validateSid(sid)) {
    throw new Error(`Source Id is invalid`);
  }
  let match = sidRegEx.exec(sid);
  console.log(`parseSid: ${sid}  ${match}`)
  let net = match[1];
  let sta = match[3] ? match[3] : '';
  let loc = match[5] ? match[5] : '';
  let band = match[8] ? match[8] : '';
  let source = match[9] ? match[9] : '';
  let subsource = match[10] ? match[10] : '';
  let out = {
    sid: {
      net: net,
      tempNetCode: null,
      tempNetYear: null,
      sta: sta,
      loc: loc,
      band: band,
      source: source,
      subsource: subsource
    },
    seed: {
      net: '',
      sta: sta,
      loc: loc,
      chan: ''
    },
    reason: ''
  };
  const tempNetMatch = tempNetRegEx.exec(net);
  if (tempNetMatch) {
    out.sid.tempNetCode = tempNetMatch[1];
    out.sid.tempNetYear = tempNetMatch[2];
    out.seed.net = out.sid.tempNetCode;
  } else if (out.sid.net.length < 3) {
    out.seed.net = out.sid.net;
  } else {
    out.reason += `network code > 2 chars: '${out.sid.net}'. `;
    out.seed = null;
  }
  if (out.sid.sta.length <= 5) {
    if (out.seed) { out.seed.sta = out.sid.sta; }
  } else {
    out.reason += `station codes > 5 chars: '${out.sid.sta}'. `;
    out.seed = null;
  }
  if (out.sid.loc.length <= 2) {
    if (out.seed) { out.seed.loc = out.sid.loc; }
  } else {
    out.reason += `loc codes > 2 chars: '${out.sid.loc}'. `;
    out.seed = null;
  }
  if (band.length === 1 && source.length === 1 && subsource.length === 1) {
    if (out.seed) { out.seed.chan = `${band}${source}${subsource}`; }
  } else {
    console.log(`band: ${band} s: ${source} ss: ${subsource}`)
    out.seed = null;
    if (band.length !== 1) {
      out.reason += `band code not 1 chars: '${out.sid.band}'. `;
    }
    if (source.length !== 1) {
      out.reason += `source code not 1 chars: '${out.sid.source}'. `;
    }
    if (subsource.length !== 1) {
      out.reason += `subsource code not 1 chars: '${out.sid.subsource}'. `;
    }
  }
  if (out.seed && ! validateNSLC(out.seed.net, out.seed.sta, out.seed.loc, out.seed.chan)) {
    out.reason += `NSLC codes invalid: '${out.seed.net}', '${out.seed.sta}', '${out.seed.loc}', '${out.seed.chan}'. `;
    out.seed = null;
  }
  return out;
}

function parsedToSid(parsedSid) {
  if (!parsedSid.net) {
    throw new Error(`network must not be empty`);
  }
  let sid = `${fdsnPrefix}${parsedSid.net}`;
  if (parsedSid.sta !== null && parsedSid.sta.length > 0) {
    sid = `${sid}${sep}${parsedSid.sta}`;
    if (parsedSid.loc !== null) {
      sid = `${sid}${sep}${parsedSid.loc}`;
      if (parsedSid.source && parsedSid.source.length > 0) {
        const b = parsedSid.band ? parsedSid.band : '';
        const ss = parsedSid.subsource ? parsedSid.subsource : '';
        sid = `${sid}${sep}${b}${sep}${parsedSid.source}${sep}${ss}`;
      }
    } else {
      console.log(`loc is null in ${JSON.stringify(parsedSid)}`)
    }
  }
  if (!validateSid(sid)) {
    throw new Error(`Resulting Source Id is invalid: ${sid}`);
  }
  return sid;
}

function sidToNSLC(sid) {
  if ( ! validateSid(sid)) {
    throw new Error(`Source Id is invalid`);
  }
  const parsed = parseSid(sid);
  return parsed.seed;
}
