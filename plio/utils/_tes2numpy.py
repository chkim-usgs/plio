def tes2numpy(msb_type, num_bytes, nelems=1):
    """
    Converts a MSB data type to a numpy datatype

    """
    valid_bytes = {
        'MSB_UNSIGNED_INTEGER': [1,2,4,8,16,32,64],
        'MSB_INTEGER': [1,2,4,8,16,32,64],
        'IEEE_REAL': [1,2,4,8,16,32,64],
        'CHARACTER': range(1,128),
        'MSB_BIT_STRING': range(1,128)
    }

    msb_bit_string_type = [('byte{}'.format(i), '>u1') for i in range(num_bytes)]

    dtype_map = {
        'MSB_UNSIGNED_INTEGER': '>u{}'.format(num_bytes),
        'MSB_INTEGER': '>i{}'.format(num_bytes),
        'IEEE_REAL': '>f{}'.format(num_bytes),
        'CHARACTER': 'a{}'.format(num_bytes),
        'MSB_BIT_STRING': msb_bit_string_type
    }

    if num_bytes not in valid_bytes[msb_type] and nelems == 1:
        raise Exception('invalid byte ({}) count for type ({})'.format(num_bytes, msb_type))

    if nelems > 1:
        # Must be an array
        return [('elem{}'.format(i), dtype_map[msb_type]) for i in range(nelems)]


    return dtype_map[msb_type]


tes_dtype_map = {'ATM': [('sclk_time', '>u4'),
  ('srf_pressure', '>u2'),
  ('nadir_pt',
   [('elem0', '>u2'),
    ('elem1', '>u2'),
    ('elem2', '>u2'),
    ('elem3', '>u2'),
    ('elem4', '>u2'),
    ('elem5', '>u2'),
    ('elem6', '>u2'),
    ('elem7', '>u2'),
    ('elem8', '>u2'),
    ('elem9', '>u2'),
    ('elem10', '>u2'),
    ('elem11', '>u2'),
    ('elem12', '>u2'),
    ('elem13', '>u2'),
    ('elem14', '>u2'),
    ('elem15', '>u2'),
    ('elem16', '>u2'),
    ('elem17', '>u2'),
    ('elem18', '>u2'),
    ('elem19', '>u2'),
    ('elem20', '>u2'),
    ('elem21', '>u2'),
    ('elem22', '>u2'),
    ('elem23', '>u2'),
    ('elem24', '>u2'),
    ('elem25', '>u2'),
    ('elem26', '>u2'),
    ('elem27', '>u2'),
    ('elem28', '>u2'),
    ('elem29', '>u2'),
    ('elem30', '>u2'),
    ('elem31', '>u2'),
    ('elem32', '>u2'),
    ('elem33', '>u2'),
    ('elem34', '>u2'),
    ('elem35', '>u2'),
    ('elem36', '>u2'),
    ('elem37', '>u2')]),
  ('co2_cont_temp', '>u2'),
  ('srf_temp_est', '>u2'),
  ('rms_pt', '>f4'),
  ('best_fit_opacities',
   [('elem0', '>i2'),
    ('elem1', '>i2'),
    ('elem2', '>i2'),
    ('elem3', '>i2'),
    ('elem4', '>i2'),
    ('elem5', '>i2'),
    ('elem6', '>i2'),
    ('elem7', '>i2'),
    ('elem8', '>i2')]),
  ('rms_opacities', '>f4'),
  ('co2_dw_flux', '>f4'),
  ('total_dw_flux', '>f4'),
  ('quality', [('byte0', '>u1'), ('byte1', '>u1')]),
  ('srf_radiance', '>i4'),
  ('version_id', 'a4')],
 'BOL': [('sclk_time', '>u4'),
  ('detector', '>u1'),
  ('tic_count', '>u1'),
  ('vbol', '>i2'),
  ('tbol', '>i2'),
  ('cal_vbol', '>f4'),
  ('lambert_alb', '>f4'),
  ('ti_bol', '>f4'),
  ('brightness_temp_bol', '>u2'),
  ('vbol_version_id', 'a2'),
  ('tbol_version_id', 'a2'),
  ('quality', [('byte0', '>u1'), ('byte1', '>u1')])],
 'GEO': [('sclk_time', '>u4'),
  ('detector', '>u1'),
  ('longitude', '>u2'),
  ('latitude', '>i2'),
  ('phase', '>u2'),
  ('emission', '>u2'),
  ('incidence', '>u2'),
  ('planetary_phase', '>u2'),
  ('heliocentric_lon', '>u2'),
  ('sub_sc_lon', '>u2'),
  ('sub_sc_lat', '>i2'),
  ('sub_solar_lon', '>u2'),
  ('sub_solar_lat', '>i2'),
  ('target_distance', '>u2'),
  ('height', '>u2'),
  ('altitude', '>u2'),
  ('local_time', '>u2'),
  ('solar_distance', '>u2'),
  ('angular_semidiameter', '>u2'),
  ('version_id', 'a4')],
 'IFG': [('sclk_time', '>u4'), ('detector', '>u1'), ('ifgm', '>i4')],
 'OBS': [('sclk_time', '>u4'),
  ('orbit', '>u2'),
  ('ock', '>u2'),
  ('ick', '>u4'),
  ('tic', '>u1'),
  ('pnt_angle', '>i2'),
  ('pnt_imc', '>u1'),
  ('pnt_view', 'a1'),
  ('scan_len', 'a1'),
  ('pckt_type', 'a1'),
  ('schedule_type', 'a1'),
  ('spc_gain', 'a1'),
  ('vbol_gain', 'a1'),
  ('tbol_gain', 'a1'),
  ('comp_pp', '>u1'),
  ('det_mask', '>u1'),
  ('class',
   [('byte0', '>u1'), ('byte1', '>u1'), ('byte2', '>u1'), ('byte3', '>u1')]),
  ('quality',
   [('byte0', '>u1'), ('byte1', '>u1'), ('byte2', '>u1'), ('byte3', '>u1')]),
  ('temps',
   [('elem0', '>u2'), ('elem1', '>u2'), ('elem2', '>u2'), ('elem3', '>u2')]),
  ('ffti', '>u1')],
 'POS': [('sclk_time', '>u4'),
  ('et', '>f8'),
  ('pos', [('elem0', '>f4'), ('elem1', '>f4'), ('elem2', '>f4')]),
  ('sun', [('elem0', '>f4'), ('elem1', '>f4'), ('elem2', '>f4')]),
  ('quat',
   [('elem0', '>f4'), ('elem1', '>f4'), ('elem2', '>f4'), ('elem3', '>f4')]),
  ('id', [('elem0', 'a1'), ('elem1', 'a1')])],
 'RAD': [('sclk_time', '>u4'),
  ('detector', '>u1'),
  ('spectral_mask', '>u1'),
  ('cmode', '>u2'),
  ('raw_rad', '>i4'),
  ('cal_rad', '>i4'),
  ('tdet', '>u2'),
  ('target_temp', '>u2'),
  ('ti_spc', '>f4'),
  ('version_id', 'a4'),
  ('quality',
   [('byte0', '>u1'), ('byte1', '>u1'), ('byte2', '>u1'), ('byte3', '>u1')])],
 'TLM': [('sclk_time', '>u4'),
  ('aux_temps',
   [('elem0', '>u2'),
    ('elem1', '>u2'),
    ('elem2', '>u2'),
    ('elem3', '>u2'),
    ('elem4', '>u2'),
    ('elem5', '>u2'),
    ('elem6', '>u2'),
    ('elem7', '>u2'),
    ('elem8', '>u2'),
    ('elem9', '>u2'),
    ('elem10', '>u2'),
    ('elem11', '>u2')]),
  ('ifgm_max',
   [('elem0', '>i2'),
    ('elem1', '>i2'),
    ('elem2', '>i2'),
    ('elem3', '>i2'),
    ('elem4', '>i2'),
    ('elem5', '>i2')]),
  ('ifgm_min',
   [('elem0', '>i2'),
    ('elem1', '>i2'),
    ('elem2', '>i2'),
    ('elem3', '>i2'),
    ('elem4', '>i2'),
    ('elem5', '>i2')]),
  ('dsp_log',
   [('elem0', '>u2'),
    ('elem1', '>u2'),
    ('elem2', '>u2'),
    ('elem3', '>u2'),
    ('elem4', '>u2'),
    ('elem5', '>u2')]),
  ('V1', '>i1'),
  ('V2', '>i1'),
  ('V3', '>i1'),
  ('V4', '>i1'),
  ('V5', '>i1'),
  ('V6', '>i1'),
  ('V7', '>i1'),
  ('V8', '>i1'),
  ('V9', '>i1'),
  ('V10', '>i1'),
  ('V11', '>i1'),
  ('V12', '>i1'),
  ('V13', '>i1'),
  ('V14', '>i1'),
  ('V15', '>i1'),
  ('V16', '>i1'),
  ('V17', '>i1'),
  ('V18', '>i1'),
  ('V19', '>i1'),
  ('V20', '>i1'),
  ('neon_lamp', '>u1'),
  ('neon_gain', 'a1'),
  ('neon_amp', '>i1'),
  ('neon_zpd', '>u2'),
  ('ifgm_zpd',
   [('elem0', '>u2'),
    ('elem1', '>u2'),
    ('elem2', '>u2'),
    ('elem3', '>u2'),
    ('elem4', '>u2'),
    ('elem5', '>u2')]),
  ('ifgm_end',
   [('elem0', '>u2'),
    ('elem1', '>u2'),
    ('elem2', '>u2'),
    ('elem3', '>u2'),
    ('elem4', '>u2'),
    ('elem5', '>u2')])]}

tes_columns = {'ATM': ['sclk_time',
  'srf_pressure',
  'nadir_pt',
  'co2_cont_temp',
  'srf_temp_est',
  'rms_pt',
  'best_fit_opacities',
  'rms_opacities',
  'co2_dw_flux',
  'total_dw_flux',
  'quality',
  'srf_radiance',
  'version_id'],
 'BOL': ['sclk_time',
  'detector',
  'tic_count',
  'vbol',
  'tbol',
  'cal_vbol',
  'lambert_alb',
  'ti_bol',
  'brightness_temp_bol',
  'vbol_version_id',
  'tbol_version_id',
  'quality'],
 'GEO': ['sclk_time',
  'detector',
  'longitude',
  'latitude',
  'phase',
  'emission',
  'incidence',
  'planetary_phase',
  'heliocentric_lon',
  'sub_sc_lon',
  'sub_sc_lat',
  'sub_solar_lon',
  'sub_solar_lat',
  'target_distance',
  'height',
  'altitude',
  'local_time',
  'solar_distance',
  'angular_semidiameter',
  'version_id'],
 'IFG': ['sclk_time', 'detector', 'ifgm'],
 'OBS': ['sclk_time',
  'orbit',
  'ock',
  'ick',
  'tic',
  'pnt_angle',
  'pnt_imc',
  'pnt_view',
  'scan_len',
  'pckt_type',
  'schedule_type',
  'spc_gain',
  'vbol_gain',
  'tbol_gain',
  'comp_pp',
  'det_mask',
  'class',
  'quality',
  'temps',
  'ffti'],
 'POS': ['sclk_time', 'et', 'pos', 'sun', 'quat', 'id'],
 'RAD': ['sclk_time',
  'detector',
  'spectral_mask',
  'cmode',
  'raw_rad',
  'cal_rad',
  'tdet',
  'target_temp',
  'ti_spc',
  'version_id',
  'quality'],
 'TLM': ['sclk_time',
  'aux_temps',
  'ifgm_max',
  'ifgm_min',
  'dsp_log',
  'V1',
  'V2',
  'V3',
  'V4',
  'V5',
  'V6',
  'V7',
  'V8',
  'V9',
  'V10',
  'V11',
  'V12',
  'V13',
  'V14',
  'V15',
  'V16',
  'V17',
  'V18',
  'V19',
  'V20',
  'neon_lamp',
  'neon_gain',
  'neon_amp',
  'neon_zpd',
  'ifgm_zpd',
  'ifgm_end']}

tes_scaling_factors = {'ATM': {'best_fit_opacities': 0.001,
  'co2_cont_temp': 0.01,
  'nadir_pt': 0.01,
  'srf_pressure': 0.001,
  'srf_temp_est': 0.01},
 'BOL': {'brightness_temp_bol': 0.01,
  'tbol': 0.000152587890625,
  'vbol': 0.000152587890625},
 'CMP': {},
 'GEO': {'angular_semidiameter': 0.01,
  'emission': 0.01,
  'height': 0.01,
  'heliocentric_lon': 0.01,
  'incidence': 0.01,
  'latitude': 0.01,
  'local_time': 0.001,
  'longitude': 0.01,
  'phase': 0.01,
  'planetary_phase': 0.01,
  'solar_distance': 10000,
  'sub_sc_lat': 0.01,
  'sub_sc_lon': 0.01,
  'sub_solar_lat': 0.01,
  'sub_solar_lon': 0.01},
 'IFG': {},
 'OBS': {'pnt_angle': 0.046875, 'temps': 0.01},
 'PCT': {},
 'POS': {},
 'RAD': {'target_temp': 0.01, 'tdet': 0.01},
 'TLM': {'V1': 3.90625,
  'V10': -0.15625,
  'V11': 0.0976055,
  'V12': -0.0985813,
  'V13': 0.976562,
  'V14': 0.0648437,
  'V15': 0.045727,
  'V16': 0.0480992,
  'V17': 0.0478277,
  'V18': 0.0488039,
  'V19': 0.141966,
  'V2': 1.95312,
  'V20': -0.149688,
  'V3': 0.278906,
  'V4': 0.278906,
  'V5': 4.45312,
  'V6': 0.652344,
  'V7': 0.119457,
  'V8': -0.103067,
  'V9': 0.15576,
  'aux_temps': 0.01,
  'ifgm_max': 0.000152587890625,
  'ifgm_min': 0.000152587890625}}
