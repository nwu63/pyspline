# =============================================================================
# Standard Python modules                                           
# =============================================================================
import os, sys

# =============================================================================
# External Python modules
# =============================================================================
import numpy

# =============================================================================
# Extension modules
# =============================================================================
from mdo_regression_helper import *
from pyspline import pySpline

def run_volume_test(volume):
    ''' This function is used to test the functions that are apart of
    the curve class. They operate on the 'curve' that is passed. '''

    # ----------- Evaluation and derivative functions ---------------
    pts = [[0,0,0],[1,1,1],[.25,.5,.95]]
    for pt in pts:
        print('Testing pt (%f %f)'%(pt[0],pt[1]))
        print('Value:')
        reg_write(volume(pt[0], pt[1], pt[2]),1e-10,1e-10)

    print('Get value corner')
    for i in range(8):
        print('Pt %d'%(i))
        reg_write(volume.getOrigValueCorner(i))

    print('Get Value edge:')
    for i in range(12):
        print('Edge %d'%(i))
        reg_write(volume.getValueEdge(i, 0.25))
        reg_write(volume.getValueEdge(i, 0.75))

    if volume.origData:
        print('Orig values at each corner')
        for i in range(8):
            reg_write(volume.getOrigValueCorner(i))

        print('GetOrigValuesFace')
        for i in range(6):
            reg_write(volume.getOrigValuesFace(i))

        print('getMidPointEdge')
        for i in range(12):
            reg_write(volume.getMidPointEdge(i))

        print('getMidPointFace')
        for i in range(6):
            reg_write(volume.getMidPointFace(i))


    print('Test get bounds')
    reg_write(volume.getBounds())
    

def run_project_test(volume):
    # Run a bunch of point projections: Tolerance for projections is
    # 1e-10, so only enforce that things match to 1e-8 or 100*eps
    eps = 1e-8

    print('------------- These points should be fully inside of domain')
    pts= [[0,0,0],[.025,.09,.3],[.2,.3,.1]]
    for pt in pts:
        print('Projecting point (%f %f %f)'%(pt[0],pt[1],pt[2]))
        u,v,w,D = volume.projectPoint(pt)
        print('u:')
        reg_write(u, eps, eps)
        print('v:')
        reg_write(v, eps, eps)
        print('w:')
        reg_write(w, eps, eps)
        print('D:')
        reg_write(D, eps, eps)

def io_test(volume):
    '''Test the writing functions'''
    volume.writeTecplot('tmp.dat', vols=True, coef=True, orig=True)

    f = open('tmp.dat','w')
    # These three calls, are private functions normally only called
    # from pyGeo. We are not checking their output, rather just making
    # sure they run. 

    os.remove('tmp.dat')

    return


# Define raw data for a volume:
data = numpy.array([
-0.3820033967	,	-0.317065736	,	-0.2513391755	,
-0.1851343782	,	-0.1188180469	,	-5.28E-002	,
1.26E-002	,	7.70E-002	,	0.1401384026	,
-0.3932057743	,	-0.3291042044	,	-0.2643126055	,
-0.1990745251	,	-0.1337139679	,	-6.86E-002	,
-3.96E-003	,	5.98E-002	,	0.1224586266	,
-0.3982453538	,	-0.3345994825	,	-0.2703624532	,
-0.2057106976	,	-0.1409255225	,	-7.63E-002	,
-1.21E-002	,	5.14E-002	,	0.1139847854	,
-0.3968382067	,	-0.3331395919	,	-0.2689486899	,
-0.204374817	,	-0.1396565819	,	-7.50E-002	,
-1.07E-002	,	5.30E-002	,	0.116025209	,
-0.3886171128	,	-0.3243518871	,	-0.2596932448	,
-0.194683387	,	-0.1295182242	,	-6.44E-002	,
5.25E-004	,	6.50E-002	,	0.1289905189	,
-0.3739524559	,	-0.3086126955	,	-0.2429783893	,
-0.1770246228	,	-0.1109046086	,	-4.48E-002	,
2.13E-002	,	8.71E-002	,	0.1524627817	,
-0.3531409204	,	-0.2863467276	,	-0.2193568597	,
-0.1520792869	,	-8.46E-002	,	-1.71E-002	,
5.05E-002	,	0.1178783374	,	0.1851211041	,
-0.3648283255	,	-0.2996971829	,	-0.2338293065	,
-0.1675525862	,	-0.1012479499	,	-3.53E-002	,
2.99E-002	,	9.40E-002	,	0.1567156358	,
-0.3759475906	,	-0.3117706865	,	-0.2469029548	,
-0.1816534061	,	-0.1163527064	,	-5.14E-002	,
1.30E-002	,	7.65E-002	,	0.1387630463	,
-0.3809990757	,	-0.3174731936	,	-0.2533015669	,
-0.1887788787	,	-0.12418278	,	-5.98E-002	,
4.04E-003	,	6.71E-002	,	0.1292838964	,
-0.3796395106	,	-0.3164090402	,	-0.2525820463	,
-0.1884326434	,	-0.1241920866	,	-6.01E-002	,
3.59E-003	,	6.67E-002	,	0.129031032	,
-0.3716045457	,	-0.3082586168	,	-0.2443647718	,
-0.1801773676	,	-0.1158769801	,	-5.17E-002	,
1.23E-002	,	7.58E-002	,	0.138750918	,
-0.3571503913	,	-0.2933382804	,	-0.2290252145	,
-0.1644506676	,	-9.97E-002	,	-3.51E-002	,
2.95E-002	,	9.38E-002	,	0.1576941568	,
-0.3365952071	,	-0.2720185883	,	-0.2069909509	,
-0.1417305805	,	-7.63E-002	,	-1.09E-002	,
5.46E-002	,	0.1199471979	,	0.1851211	,
-0.3508339644	,	-0.2859033601	,	-0.2202948782	,
-0.1543572994	,	-8.85E-002	,	-2.31E-002	,
4.15E-002	,	0.1049272902	,	0.1669071638	,
-0.3614420823	,	-0.2974665961	,	-0.2328544333	,
-0.1679300056	,	-0.1030246017	,	-3.85E-002	,
2.53E-002	,	8.81E-002	,	0.1497589835	,
-0.3660609469	,	-0.3028376789	,	-0.2390172896	,
-0.1749089247	,	-0.1107872242	,	-4.70E-002	,
1.63E-002	,	7.87E-002	,	0.1401831068	,
-0.3643714474	,	-0.30165623	,	-0.2383917224	,
-0.1748593221	,	-0.1112902596	,	-4.79E-002	,
1.50E-002	,	7.73E-002	,	0.1388096434	,
-0.3560165482	,	-0.293550231	,	-0.2305812279	,
-0.1673648097	,	-0.1040802305	,	-4.09E-002	,
2.19E-002	,	8.44E-002	,	0.1461955578	,
-0.3413378609	,	-0.2788751093	,	-0.2159529828	,
-0.1528103757	,	-8.96E-002	,	-2.64E-002	,
3.67E-002	,	9.94E-002	,	0.1618646916	,
-0.3206747427	,	-0.2580142177	,	-0.19494358	,
-0.1316727357	,	-6.83E-002	,	-4.84E-003	,
5.86E-002	,	0.1219277798	,	0.1851211	,
-0.3405181244	,	-0.2760956296	,	-0.2110764496	,
-0.1458043929	,	-8.07E-002	,	-1.61E-002	,
4.75E-002	,	0.1099442124	,	0.1708441246	,
-0.3502538927	,	-0.2867135838	,	-0.2225955318	,
-0.1582334356	,	-9.40E-002	,	-3.02E-002	,
3.29E-002	,	9.48E-002	,	0.1555576042	,
-0.3540912988	,	-0.2913300724	,	-0.2280075761	,
-0.1644610541	,	-0.1009608074	,	-3.78E-002	,
2.47E-002	,	8.63E-002	,	0.1469340517	,
-0.3516812882	,	-0.2895753928	,	-0.2269371145	,
-0.1640885193	,	-0.1012553847	,	-3.87E-002	,
2.34E-002	,	8.48E-002	,	0.1454589901	,
-0.3427231052	,	-0.2811427781	,	-0.2190571148	,
-0.1567754358	,	-9.45E-002	,	-3.23E-002	,
2.95E-002	,	9.08E-002	,	0.1516013649	,
-0.3274977878	,	-0.2663224232	,	-0.2046638293	,
-0.142833206	,	-8.09E-002	,	-1.91E-002	,
4.26E-002	,	0.1039425258	,	0.1649708519	,
-0.3063722313	,	-0.2454902886	,	-0.1841561505	,
-0.1226639784	,	-6.11E-002	,	5.61E-004	,
6.22E-002	,	0.1237134884	,	0.1851211	,
-0.3341574914	,	-0.2705299631	,	-0.2063756346	,
-0.1420534089	,	-7.80E-002	,	-1.45E-002	,
4.79E-002	,	0.1090216279	,	0.1685584773	,
-0.3427244182	,	-0.2798086402	,	-0.2163774991	,
-0.1527731233	,	-8.93E-002	,	-2.64E-002	,
3.56E-002	,	9.65E-002	,	0.1561591731	,
-0.3454558988	,	-0.2832517567	,	-0.220540397	,
-0.1576653792	,	-9.49E-002	,	-3.26E-002	,
2.91E-002	,	8.99E-002	,	0.1495159347	,
-0.3420318035	,	-0.2805289018	,	-0.2185434795	,
-0.1563955633	,	-9.43E-002	,	-3.25E-002	,
2.87E-002	,	8.93E-002	,	0.148992852	,
-0.3321640722	,	-0.271360479	,	-0.2100966088	,
-0.1486721982	,	-8.73E-002	,	-2.60E-002	,
3.48E-002	,	9.52E-002	,	0.1549704104	,
-0.3161010218	,	-0.255998621	,	-0.1954516002	,
-0.1347589064	,	-7.40E-002	,	-1.34E-002	,
4.71E-002	,	0.1072893728	,	0.1671217249	,
-0.2942588862	,	-0.234847089	,	-0.1750182312	,
-0.1150452466	,	-5.50E-002	,	5.12E-003	,
6.52E-002	,	0.125218427	,	0.1851211	,
-0.33200338	,	-0.2693651633	,	-0.2062833438	,
-0.1431233937	,	-8.03E-002	,	-1.82E-002	,
4.28E-002	,	0.1024301466	,	0.1604007521	,
-0.3391162459	,	-0.276930489	,	-0.214309303	,
-0.1515889074	,	-8.91E-002	,	-2.73E-002	,
3.37E-002	,	9.35E-002	,	0.151869752	,
-0.3404902221	,	-0.2788571585	,	-0.2167927249	,
-0.1546266456	,	-9.26E-002	,	-3.11E-002	,
2.97E-002	,	8.95E-002	,	0.1481754043	,
-0.3358107904	,	-0.2748310305	,	-0.2134446492	,
-0.1519436702	,	-9.06E-002	,	-2.95E-002	,
3.10E-002	,	9.07E-002	,	0.1495813514	,
-0.3247692447	,	-0.2645697854	,	-0.2039853863	,
-0.1432744245	,	-8.26E-002	,	-2.22E-002	,
3.79E-002	,	9.74E-002	,	0.1563853751	,
-0.3076683991	,	-0.248365358	,	-0.1886908254	,
-0.1288939074	,	-6.91E-002	,	-9.36E-003	,
5.02E-002	,	0.1094196747	,	0.1683116438	,
-0.2849071181	,	-0.2265951924	,	-0.1679401017	,
-0.1091501515	,	-5.03E-002	,	8.63E-003	,
6.75E-002	,	0.1263729404	,	0.1851211	,
-0.3341574881	,	-0.2726552636	,	-0.2108043328	,
-0.1489749816	,	-8.75E-002	,	-2.70E-002	,
3.24E-002	,	9.04E-002	,	0.1466321666	,
-0.3396351973	,	-0.2782317077	,	-0.2164825652	,
-0.1547187777	,	-9.33E-002	,	-3.25E-002	,
2.73E-002	,	8.58E-002	,	0.1429075489	,
-0.3394735472	,	-0.2783707561	,	-0.2169204278	,
-0.1554416014	,	-9.42E-002	,	-3.35E-002	,
2.64E-002	,	8.53E-002	,	0.1430861395	,
-0.3333594187	,	-0.272768383	,	-0.2118527532	,
-0.150882153	,	-9.01E-002	,	-2.97E-002	,
3.01E-002	,	8.92E-002	,	0.1473508775	,
-0.3210007121	,	-0.2611713658	,	-0.2010366882	,
-0.1408217524	,	-8.07E-002	,	-2.08E-002	,
3.86E-002	,	9.76E-002	,	0.1559230464	,
-0.3027108756	,	-0.24387376	,	-0.1847406961	,
-0.1255214569	,	-6.63E-002	,	-7.21E-003	,
5.17E-002	,	0.110304162	,	0.1685722771	,
-0.278877907	,	-0.2212355141	,	-0.1633244097	,
-0.1053012311	,	-4.72E-002	,	1.09E-002	,
6.90E-002	,	0.127115541	,	0.1851211	,
-0.3405181241	,	-0.2802794626	,	-0.2198020707	,
-0.1594546784	,	-9.96E-002	,	-4.07E-002	,
1.70E-002	,	7.31E-002	,	0.1274985762	,
-0.3441946194	,	-0.2836077785	,	-0.2227794576	,
-0.162029841	,	-0.1016720423	,	-4.21E-002	,
1.64E-002	,	7.37E-002	,	0.1294813056	,
-0.3423570726	,	-0.2817247256	,	-0.2208423887	,
-0.1600135605	,	-9.95E-002	,	-3.96E-002	,
1.95E-002	,	7.76E-002	,	0.134416174	,
-0.334680098	,	-0.2743220533	,	-0.2137344738	,
-0.1531604853	,	-9.28E-002	,	-3.29E-002	,
2.64E-002	,	8.48E-002	,	0.1424244818	,
-0.3209333933	,	-0.261214183	,	-0.2012815992	,
-0.1413240708	,	-8.15E-002	,	-2.20E-002	,
3.71E-002	,	9.57E-002	,	0.1536589757	,
-0.301401691	,	-0.242662778	,	-0.1837151265	,
-0.1247265936	,	-6.58E-002	,	-6.96E-003	,
5.16E-002	,	0.1099554934	,	0.1679354037	,
-0.2764817663	,	-0.2190295774	,	-0.1613941146	,
-0.1036785217	,	-4.59E-002	,	1.19E-002	,
6.97E-002	,	0.1274154737	,	0.1851211	,
-0.3508339712	,	-0.2919957952	,	-0.2330496817	,
-0.174348004	,	-0.1162463644	,	-5.92E-002	,
-3.39E-003	,	5.08E-002	,	0.1031687398	,
-0.3526162757	,	-0.2928984574	,	-0.2330613094	,
-0.1734014038	,	-0.1142174181	,	-5.59E-002	,
1.34E-003	,	5.72E-002	,	0.1116424388	,
-0.3489631682	,	-0.2887633126	,	-0.2284261519	,
-0.1682288684	,	-0.10839119	,	-4.93E-002	,
9.02E-003	,	6.62E-002	,	0.1222101193	,
-0.339643169	,	-0.2793766673	,	-0.2189879881	,
-0.1586849958	,	-9.87E-002	,	-3.91E-002	,
1.97E-002	,	7.78E-002	,	0.1348843936	,
-0.3244242072	,	-0.2645888296	,	-0.2046414948	,
-0.1447272358	,	-8.50E-002	,	-2.56E-002	,
3.34E-002	,	9.18E-002	,	0.1495585704	,
-0.3036227519	,	-0.2446452298	,	-0.1855527979	,
-0.1264666582	,	-6.74E-002	,	-8.60E-003	,
5.00E-002	,	0.1083736472	,	0.1663884056	,
-0.2776400833	,	-0.2199262769	,	-0.1621184132	,
-0.1042634158	,	-4.64E-002	,	1.15E-002	,
6.94E-002	,	0.1272780167	,	0.1851211	,
-0.3648283249	,	-0.3075318428	,	-0.2502652355	,
-0.1933694672	,	-0.1371735692	,	-8.21E-002	,
-2.84E-002	,	2.37E-002	,	7.40E-002	,
-0.3645718507	,	-0.3057707675	,	-0.2469759267	,
-0.1884642373	,	-0.1305135565	,	-7.35E-002	,
-1.76E-002	,	3.69E-002	,	8.99E-002	,
-0.3590199475	,	-0.299227792	,	-0.2394108403	,
-0.1798229093	,	-0.1206659037	,	-6.23E-002	,
-4.77E-003	,	5.16E-002	,	0.1067733153	,
-0.3479411178	,	-0.2876613005	,	-0.2273628893	,
-0.1672204395	,	-0.1074194787	,	-4.82E-002	,
1.04E-002	,	6.81E-002	,	0.1249105835	,
-0.3312180185	,	-0.2710564305	,	-0.2108769303	,
-0.1507821091	,	-9.09E-002	,	-3.14E-002	,
2.76E-002	,	8.61E-002	,	0.1439384806	,
-0.3091312629	,	-0.2496249262	,	-0.1900865393	,
-0.1305906048	,	-7.12E-002	,	-1.20E-002	,
4.70E-002	,	0.1056609614	,	0.164019252	,
-0.2820786537	,	-0.2237162394	,	-0.165334418	,
-0.1069228497	,	-4.85E-002	,	9.91E-003	,
6.83E-002	,	0.1267339023	,	0.1851211	,
-0.3820033967	,	-0.3264209141	,	-0.2710312369	,
-0.2161444363	,	-0.1620550476	,	-0.1091528647	,
-5.77E-002	,	-7.84E-003	,	4.01E-002	,
-0.3795267143	,	-0.3217430891	,	-0.2641030032	,
-0.2068587329	,	-0.1502543179	,	-9.47E-002	,
-4.02E-002	,	1.28E-002	,	6.43E-002	,
-0.371894213	,	-0.3125288303	,	-0.2532494916	,
-0.1942961932	,	-0.1358349475	,	-7.82E-002	,
-2.15E-002	,	3.41E-002	,	8.84E-002	,
-0.3589804539	,	-0.2986564136	,	-0.2384023008	,
-0.178383421	,	-0.1187539544	,	-5.97E-002	,
-1.39E-003	,	5.61E-002	,	0.1126129241	,
-0.3406262161	,	-0.2800365623	,	-0.2194945857	,
-0.1590990093	,	-9.89E-002	,	-3.92E-002	,
2.00E-002	,	7.87E-002	,	0.1367823162	,
-0.3172213515	,	-0.2569953842	,	-0.1967783771	,
-0.1366512216	,	-7.66E-002	,	-1.68E-002	,
4.27E-002	,	0.1019914082	,	0.1609517084	,
-0.2891295254	,	-0.2298481966	,	-0.1705668677	,
-0.1112855389	,	-5.20E-002	,	7.28E-003	,
6.66E-002	,	0.1258397765	,	0.1851211041	,
-0.1553480476	,	-0.1418638273	,	-0.1329900787	,
-0.129034216	,	-0.129966021	,	-0.1361547416	,
-0.147186261	,	-0.1630450634	,	-0.1833910048	,
-9.12E-002	,	-7.83E-002	,	-6.94E-002	,
-6.51E-002	,	-6.52E-002	,	-7.02E-002	,
-7.96E-002	,	-9.35E-002	,	-0.1114866918	,
-2.63E-002	,	-1.38E-002	,	-4.85E-003	,
-2.13E-005	,	7.27E-004	,	-2.91E-003	,
-1.06E-002	,	-2.24E-002	,	-3.79E-002	,
3.87E-002	,	5.08E-002	,	6.00E-002	,
6.53E-002	,	6.70E-002	,	6.47E-002	,
5.88E-002	,	4.91E-002	,	3.61E-002	,
0.1032788774	,	0.1149353717	,	0.1241254045	,
0.1299315706	,	0.1324640277	,	0.1314810598	,
0.1272363001	,	0.1196332204	,	0.1089928269	,
0.1666877738	,	0.1776847172	,	0.1867512019	,
0.1928173249	,	0.1960132285	,	0.1961290796	,
0.1933783902	,	0.1876366214	,	0.1792199945	,
0.2283531427	,	0.2384369244	,	0.2471262499	,
0.2531987186	,	0.2568044574	,	0.2577655161	,
0.2562552857	,	0.2521212161	,	0.2456747442	,
-0.1725231142	,	-0.1590295694	,	-0.1501321702	,
-0.1461524565	,	-0.1470841324	,	-0.1531738515	,
-0.1641199044	,	-0.1798232477	,	-0.199968221	,
-0.1088453619	,	-9.54E-002	,	-8.63E-002	,
-8.16E-002	,	-8.14E-002	,	-8.59E-002	,
-9.48E-002	,	-0.1080383031	,	-0.1253450103	,
-4.43E-002	,	-3.09E-002	,	-2.14E-002	,
-1.60E-002	,	-1.46E-002	,	-1.73E-002	,
-2.41E-002	,	-3.48E-002	,	-4.92E-002	,
2.06E-002	,	3.40E-002	,	4.38E-002	,
5.00E-002	,	5.26E-002	,	5.16E-002	,
4.69E-002	,	3.88E-002	,	2.73E-002	,
8.51E-002	,	9.84E-002	,	0.1084891815	,
0.1153983704	,	0.1191297008	,	0.1196995748	,
0.1171017835	,	0.1114233272	,	0.1028074992	,
0.1485947725	,	0.1616612103	,	0.1718006934	,
0.1792447046	,	0.183944422	,	0.1859806623	,
0.1852722601	,	0.1818997686	,	0.1759677558	,
0.2104077217	,	0.2230025798	,	0.233007928	,
0.2407613169	,	0.2462083161	,	0.249484569	,
0.2504408463	,	0.249149752	,	0.24567474	,
-0.1865174669	,	-0.1726744707	,	-0.1634185202	,
-0.1590241272	,	-0.1595099222	,	-0.165127796	,
-0.1755356881	,	-0.1906651864	,	-0.2101597429	,
-0.1234614504	,	-0.1095750037	,	-9.99E-002	,
-9.46E-002	,	-9.36E-002	,	-9.73E-002	,
-0.105350499	,	-0.1176281046	,	-0.1338793168	,
-5.94E-002	,	-4.54E-002	,	-3.52E-002	,
-2.90E-002	,	-2.66E-002	,	-2.83E-002	,
-3.39E-002	,	-4.33E-002	,	-5.63E-002	,
5.12E-003	,	1.91E-002	,	2.98E-002	,
3.70E-002	,	4.08E-002	,	4.10E-002	,
3.79E-002	,	3.14E-002	,	2.17E-002	,
6.94E-002	,	8.34E-002	,	9.44E-002	,
0.1024994925	,	0.1076390605	,	0.109755058	,
0.1089658787	,	0.1052783755	,	9.88E-002	,
0.1327068139	,	0.146549535	,	0.1578304585	,
0.1666236452	,	0.1729716577	,	0.1768208917	,
0.1782378714	,	0.1772071864	,	0.1737732404	,
0.1944872668	,	0.2079724249	,	0.2193080482	,
0.2286288386	,	0.2360004276	,	0.2413875336	,
0.2448185953	,	0.2462529365	,	0.24567474	,
-0.1968333007	,	-0.1824015974	,	-0.1724589903	,
-0.1673568695	,	-0.1670673104	,	-0.1718780595	,
-0.1814167356	,	-0.1956011855	,	-0.2140967014	,
-0.1347380575	,	-0.1201497097	,	-0.1096584086	,
-0.1034941006	,	-0.1016305042	,	-0.1042994734	,
-0.1112017314	,	-0.122270067	,	-0.1371988203	,
-7.15E-002	,	-5.68E-002	,	-4.57E-002	,
-3.85E-002	,	-3.51E-002	,	-3.56E-002	,
-3.98E-002	,	-4.78E-002	,	-5.91E-002	,
-7.73E-003	,	7.13E-003	,	1.87E-002	,
2.69E-002	,	3.19E-002	,	3.35E-002	,
3.19E-002	,	2.70E-002	,	1.92E-002	,
5.59E-002	,	7.08E-002	,	8.28E-002	,
9.20E-002	,	9.85E-002	,	0.1021125851	,
0.1030140446	,	0.1011858999	,	9.69E-002	,
0.1187887568	,	0.1335780378	,	0.1458524683	,
0.1558938879	,	0.1637181321	,	0.169249037	,
0.1725631326	,	0.1736189247	,	0.1726237007	,
0.1801847641	,	0.194717599	,	0.2071412521	,
0.217850599	,	0.2268753032	,	0.234149515	,
0.239716127	,	0.2434961634	,	0.24567474	,
-0.2031939299	,	-0.1878709651	,	-0.1770024238	,
-0.1709138214	,	-0.1695802524	,	-0.1732772988	,
-0.1816449467	,	-0.1946023832	,	-0.2118110554	,
-0.1423526839	,	-0.1268721283	,	-0.1154146457	,
-0.1081999673	,	-0.105202646	,	-0.1066400198	,
-0.1122267432	,	-0.1218927224	,	-0.135334093	,
-8.03E-002	,	-6.47E-002	,	-5.27E-002	,
-4.44E-002	,	-3.97E-002	,	-3.89E-002	,
-4.18E-002	,	-4.82E-002	,	-5.78E-002	,
-1.75E-002	,	-1.85E-003	,	1.06E-002	,
2.00E-002	,	2.62E-002	,	2.92E-002	,
2.91E-002	,	2.59E-002	,	1.99E-002	,
4.53E-002	,	6.09E-002	,	7.38E-002	,
8.41E-002	,	9.18E-002	,	9.69E-002	,
9.94E-002	,	9.94E-002	,	9.70E-002	,
0.1073428802	,	0.1228204812	,	0.1360190748	,
0.1471767494	,	0.1563159525	,	0.1633618168	,
0.1683939081	,	0.1713741932	,	0.172491542	,
0.1680714262	,	0.1832827983	,	0.1966646725	,
0.2085497112	,	0.2189815312	,	0.2278827387	,
0.2353108536	,	0.2411870707	,	0.24567474	,
-0.20534804	,	-0.1889806732	,	-0.1769969688	,
-0.1697173405	,	-0.1671238972	,	-0.16949556	,
-0.1764691415	,	-0.1879654693	,	-0.2036533351	,
-0.1460003506	,	-0.1295640066	,	-0.1170373289	,
-0.1086576035	,	-0.1044032239	,	-0.1044889211	,
-0.1086312285	,	-0.1167575466	,	-0.1285750181	,
-8.53E-002	,	-6.89E-002	,	-5.59E-002	,
-4.65E-002	,	-4.06E-002	,	-3.85E-002	,
-3.98E-002	,	-4.47E-002	,	-5.27E-002	,
-2.38E-002	,	-7.47E-003	,	5.90E-003	,
1.63E-002	,	2.37E-002	,	2.79E-002	,
2.93E-002	,	2.77E-002	,	2.35E-002	,
3.78E-002	,	5.40E-002	,	6.77E-002	,
7.89E-002	,	8.77E-002	,	9.41E-002	,
9.81E-002	,	9.97E-002	,	9.91E-002	,
9.89E-002	,	0.1147574556	,	0.1286403234	,
0.1406714169	,	0.1508807472	,	0.1591972111	,
0.1657015098	,	0.1703583887	,	0.1733369986	,
0.1587196638	,	0.1742255883	,	0.1882378555	,
0.2009641581	,	0.2124640076	,	0.2226545272	,
0.2316024759	,	0.2392284601	,	0.24567474	,
-0.2031939332	,	-0.1856799219	,	-0.17246443	,
-0.1638512343	,	-0.1598382791	,	-0.1606941988	,
-0.1660778499	,	-0.1759147237	,	-0.1898847579	,
-0.1455060902	,	-0.1280997101	,	-0.1144865761	,
-0.1048964187	,	-9.93E-002	,	-9.80E-002	,
-0.100564671	,	-0.1070485458	,	-0.1171392908	,
-8.64E-002	,	-6.92E-002	,	-5.53E-002	,
-4.48E-002	,	-3.78E-002	,	-3.43E-002	,
-3.42E-002	,	-3.74E-002	,	-4.37E-002	,
-2.63E-002	,	-9.45E-003	,	4.62E-003	,
1.59E-002	,	2.43E-002	,	2.98E-002	,
3.25E-002	,	3.25E-002	,	2.99E-002	,
3.40E-002	,	5.05E-002	,	6.46E-002	,
7.66E-002	,	8.63E-002	,	9.37E-002	,
9.89E-002	,	0.1019889179	,	0.1030123675	,
9.39E-002	,	0.10983462	,	0.12402082	,
0.1365813418	,	0.1475313648	,	0.156816865	,
0.1644997829	,	0.1705530349	,	0.1751181929	,
0.1526904562	,	0.1680629936	,	0.1822238852	,
0.1953488415	,	0.2074881581	,	0.2185667288	,
0.2286417194	,	0.2376402235	,	0.24567474	,
-0.196833301	,	-0.1780990638	,	-0.1635489699	,
-0.1534757961	,	-0.1478893459	,	-0.1470681187	,
-0.1506842139	,	-0.1586800557	,	-0.1707511789	,
-0.1408997307	,	-0.1225509597	,	-0.1078509625	,
-9.70E-002	,	-9.01E-002	,	-8.72E-002	,
-8.82E-002	,	-9.30E-002	,	-0.1012317782	,
-8.34E-002	,	-6.56E-002	,	-5.09E-002	,
-3.95E-002	,	-3.13E-002	,	-2.65E-002	,
-2.50E-002	,	-2.66E-002	,	-3.12E-002	,
-2.49E-002	,	-7.77E-003	,	6.80E-003	,
1.87E-002	,	2.81E-002	,	3.46E-002	,
3.86E-002	,	4.00E-002	,	3.89E-002	,
3.40E-002	,	5.04E-002	,	6.48E-002	,
7.71E-002	,	8.75E-002	,	9.57E-002	,
0.1020065896	,	0.1063079779	,	0.1087547062	,
9.26E-002	,	0.1081786096	,	0.1222633955	,
0.1349747157	,	0.1463115252	,	0.1562345563	,
0.1647795058	,	0.1719305667	,	0.177794627	,
0.150294317	,	0.1649998385	,	0.1787978735	,
0.1918366228	,	0.2041546999	,	0.2156860119	,
0.2264673915	,	0.2364386003	,	0.24567474	,
-0.1865174601	,	-0.1664985856	,	-0.1504917632	,
-0.1388235308	,	-0.1315142929	,	-0.1288157165	,
-0.1304784166	,	-0.1364332321	,	-0.1464213572	,
-0.1324044623	,	-0.1131455728	,	-9.73E-002	,
-8.52E-002	,	-7.69E-002	,	-7.24E-002	,
-7.17E-002	,	-7.46E-002	,	-8.10E-002	,
-7.67E-002	,	-5.83E-002	,	-4.29E-002	,
-3.06E-002	,	-2.13E-002	,	-1.52E-002	,
-1.23E-002	,	-1.23E-002	,	-1.52E-002	,
-1.98E-002	,	-2.57E-003	,	1.23E-002	,
2.48E-002	,	3.49E-002	,	4.24E-002	,
4.75E-002	,	5.02E-002	,	5.06E-002	,
3.76E-002	,	5.37E-002	,	6.80E-002	,
8.05E-002	,	9.12E-002	,	0.1001272457	,
0.1072353021	,	0.1125865124	,	0.1162473235	,
9.49E-002	,	0.109695946	,	0.1233257887	,
0.13584487	,	0.1472325919	,	0.1574650803	,
0.1665516172	,	0.1744944818	,	0.1813469652	,
0.1514526333	,	0.1649760206	,	0.1779558127	,
0.1904629684	,	0.2025201727	,	0.2140637712	,
0.225123113	,	0.2356530955	,	0.24567474	,
-0.1725231148	,	-0.1511294059	,	-0.1335893559	,
-0.1201892279	,	-0.1110020398	,	-0.1062775556	,
-0.1057892592	,	-0.1095275766	,	-0.117223606	,
-0.1202888347	,	-0.1001116106	,	-8.32E-002	,
-6.98E-002	,	-5.99E-002	,	-5.38E-002	,
-5.13E-002	,	-5.23E-002	,	-5.67E-002	,
-6.64E-002	,	-4.76E-002	,	-3.15E-002	,
-1.83E-002	,	-7.94E-003	,	-6.48E-004	,
3.74E-003	,	5.22E-003	,	4.00E-003	,
-1.12E-002	,	5.94E-003	,	2.10E-002	,
3.39E-002	,	4.46E-002	,	5.29E-002	,
5.91E-002	,	6.29E-002	,	6.47E-002	,
4.47E-002	,	6.01E-002	,	7.41E-002	,
8.66E-002	,	9.75E-002	,	0.1067784824	,
0.1144988033	,	0.1206649837	,	0.1253469373	,
0.100549372	,	0.1142275911	,	0.1271278394	,
0.1391248728	,	0.1502632183	,	0.1604587837	,
0.1697670037	,	0.1781659775	,	0.1857151726	,
0.155891201	,	0.1678347351	,	0.1796478947	,
0.1911968099	,	0.2025982538	,	0.2137052623	,
0.2246156524	,	0.2352629723	,	0.24567474	,
-0.1553480476	,	-0.1325086532	,	-0.1132980278	,
-9.80E-002	,	-8.67E-002	,	-7.98E-002	,
-7.69E-002	,	-7.82E-002	,	-8.34E-002	,
-0.1050725156	,	-8.39E-002	,	-6.58E-002	,
-5.10E-002	,	-3.96E-002	,	-3.17E-002	,
-2.73E-002	,	-2.63E-002	,	-2.85E-002	,
-5.30E-002	,	-3.38E-002	,	-1.71E-002	,
-2.97E-003	,	8.44E-003	,	1.70E-002	,
2.28E-002	,	2.59E-002	,	2.63E-002	,
2.89E-004	,	1.74E-002	,	3.26E-002	,
4.58E-002	,	5.71E-002	,	6.61E-002	,
7.31E-002	,	7.81E-002	,	8.12E-002	,
5.45E-002	,	6.93E-002	,	8.29E-002	,
9.52E-002	,	0.1060866024	,	0.1155997806	,
0.1237313671	,	0.1305192682	,	0.1359973609	,
0.1088460733	,	0.1214220903	,	0.1333632548	,
0.1446560413	,	0.1552483312	,	0.165166717	,
0.1743860876	,	0.1829329035	,	0.1908360511	,
0.1629420668	,	0.1732836546	,	0.1836252383	,
0.1939668221	,	0.2043084059	,	0.2146499896	,
0.2249915734	,	0.2353331572	,	0.2456747442	,
8.54E-026	,	0.00E+000	,	0.00E+000	,
0.00E+000	,	0.00E+000	,	0.00E+000	,
0.00E+000	,	0.00E+000	,	-5.61E-018	,
0.00E+000	,	-1.01E-026	,	-3.57E-026	,
-1.00E-026	,	2.11E-026	,	6.45E-026	,
1.10E-025	,	1.69E-025	,	0.00E+000	,
0.00E+000	,	-9.61E-028	,	-3.42E-026	,
-1.30E-026	,	1.30E-026	,	5.31E-026	,
9.77E-026	,	-5.23E-026	,	0.00E+000	,
0.00E+000	,	-9.78E-027	,	-1.79E-026	,
-1.96E-026	,	3.88E-026	,	6.59E-026	,
5.56E-026	,	1.43E-026	,	0.00E+000	,
0.00E+000	,	6.22E-027	,	5.91E-027	,
2.11E-026	,	3.04E-028	,	-4.61E-026	,
-1.91E-026	,	-1.86E-026	,	0.00E+000	,
0.00E+000	,	-4.92E-028	,	-3.47E-027	,
-1.03E-026	,	-8.59E-027	,	7.72E-027	,
1.02E-026	,	2.46E-028	,	0.00E+000	,
0.00E+000	,	0.00E+000	,	0.00E+000	,
0.00E+000	,	0.00E+000	,	0.00E+000	,
0.00E+000	,	0.00E+000	,	0.00E+000	,
5.72E-002	,	6.05E-002	,	6.42E-002	,
6.80E-002	,	7.22E-002	,	7.66E-002	,
8.12E-002	,	8.60E-002	,	9.11E-002	,
5.28E-002	,	5.63E-002	,	5.99E-002	,
6.37E-002	,	6.77E-002	,	7.20E-002	,
7.65E-002	,	8.11E-002	,	8.59E-002	,
4.87E-002	,	5.23E-002	,	5.58E-002	,
5.95E-002	,	6.34E-002	,	6.75E-002	,
7.18E-002	,	7.62E-002	,	8.07E-002	,
4.49E-002	,	4.86E-002	,	5.20E-002	,
5.56E-002	,	5.93E-002	,	6.32E-002	,
6.72E-002	,	7.13E-002	,	7.55E-002	,
4.15E-002	,	4.52E-002	,	4.85E-002	,
5.19E-002	,	5.53E-002	,	5.90E-002	,
6.27E-002	,	6.65E-002	,	7.03E-002	,
3.85E-002	,	4.21E-002	,	4.52E-002	,
4.84E-002	,	5.16E-002	,	5.49E-002	,
5.83E-002	,	6.17E-002	,	6.52E-002	,
3.59E-002	,	3.94E-002	,	4.22E-002	,
4.51E-002	,	4.80E-002	,	5.10E-002	,
5.40E-002	,	5.70E-002	,	6.00E-002	,
0.11607791	,	0.1227746262	,	0.1299991916	,
0.137774603	,	0.1460664071	,	0.154899467	,
0.1641900257	,	0.1739058322	,	0.1839817207	,
0.1071836697	,	0.1140206094	,	0.1212147701	,
0.1288733705	,	0.1369622346	,	0.1455152853	,
0.1544460481	,	0.1637344965	,	0.1733214753	,
9.89E-002	,	0.1057860902	,	0.112864609	,
0.1203298723	,	0.1281407781	,	0.1363348516	,
0.1448332489	,	0.153618064	,	0.1626424659	,
9.13E-002	,	9.81E-002	,	0.105017366	,
0.1122029515	,	0.1196611482	,	0.1274118838	,
0.1353969129	,	0.1436006096	,	0.1519827091	,
8.44E-002	,	9.12E-002	,	9.77E-002	,
0.1045563461	,	0.1115583243	,	0.1187793414	,
0.1261538984	,	0.1336812043	,	0.141322266	,
7.83E-002	,	8.48E-002	,	9.10E-002	,
9.74E-002	,	0.1038356286	,	0.1104309424	,
0.1171050675	,	0.1238592832	,	0.1306687355	,
7.29E-002	,	7.91E-002	,	8.49E-002	,
9.07E-002	,	9.65E-002	,	0.1023611359	,
0.1082379642	,	0.1141224473	,	0.1200000048	,
0.1764703537	,	0.186386822	,	0.197136537	,
0.2087318977	,	0.2211270471	,	0.2343355151	,
0.2482375791	,	0.2627756906	,	0.2778479878	,
0.1630315658	,	0.173112878	,	0.1838075051	,
0.1952103801	,	0.2072767466	,	0.2200354239	,
0.2333663939	,	0.2472315639	,	0.2615412511	,
0.1504936363	,	0.1606183944	,	0.1711327555	,
0.182231033	,	0.1938587672	,	0.2060518794	,
0.2187055786	,	0.2317860721	,	0.2452253259	,
0.1389717771	,	0.1489995723	,	0.1592092848	,
0.1698706016	,	0.1809447246	,	0.1924428784	,
0.2042949506	,	0.2164716876	,	0.2289180674	,
0.128610839	,	0.138401661	,	0.1481646893	,
0.1582473309	,	0.1686100949	,	0.1792812358	,
0.1901835412	,	0.2013111293	,	0.2126140485	,
0.1193919729	,	0.1288019993	,	0.1379671359	,
0.147335282	,	0.1568530324	,	0.1665496237	,
0.1763636634	,	0.1862934945	,	0.1963135362	,
0.1113259461	,	0.120205784	,	0.1286392146	,
0.1371434238	,	0.145680656	,	0.1542504583	,
0.1628293436	,	0.1714148623	,	0.1800000072	,
0.2379452017	,	0.2509428941	,	0.2650787984	,
0.2803713608	,	0.2967510624	,	0.314223115	,
0.3326244563	,	0.351870589	,	0.3718236859	,
0.2200149359	,	0.2331877398	,	0.247246855	,
0.2622650193	,	0.2781809257	,	0.2950223679	,
0.312629819	,	0.3309464202	,	0.3498520011	,
0.2032781264	,	0.2164668936	,	0.2302850313	,
0.2448820308	,	0.2601903916	,	0.2762495733	,
0.2929242808	,	0.3101650861	,	0.3278821021	,
0.1879063344	,	0.2009208157	,	0.2143290948	,
0.2283254079	,	0.2428698806	,	0.25797124	,
0.273544358	,	0.2895475566	,	0.3059097163	,
0.1740984823	,	0.186749784	,	0.1995566109	,
0.2127610715	,	0.2263291125	,	0.2402943638	,
0.2545661595	,	0.2691356818	,	0.2839399897	,
0.1618483947	,	0.1739401267	,	0.185939264	,
0.1981661515	,	0.2105749275	,	0.2232027278	,
0.235983909	,	0.2489169836	,	0.2619729236	,
0.1511830528	,	0.1625115094	,	0.1735200233	,
0.1845655675	,	0.195629891	,	0.2067127398	,
0.2178029399	,	0.228899645	,	0.2400000095	,
0.3000000029	,	0.315904295	,	0.3332657841	,
0.3521017507	,	0.3723163042	,	0.3939041519	,
0.4166567921	,	0.4404616865	,	0.4651444914	,
0.2777107676	,	0.2937986598	,	0.3110589509	,
0.3295358098	,	0.3491482768	,	0.3699214067	,
0.3916538442	,	0.4142690856	,	0.4376159922	,
0.2569081385	,	0.2729827599	,	0.289938682	,
0.3078750393	,	0.3267077962	,	0.3464787103	,
0.3670194429	,	0.3882642653	,	0.4101010269	,
0.2378211189	,	0.253642479	,	0.2700807519	,
0.2872500264	,	0.3051054662	,	0.3236525331	,
0.3427883244	,	0.3624582853	,	0.3825748585	,
0.2207026716	,	0.2360325261	,	0.2517115303	,
0.2678726376	,	0.2844829534	,	0.3015811886	,
0.3190602455	,	0.3369081306	,	0.3550486441	,
0.2055850193	,	0.2201709563	,	0.2348259709	,
0.2497398355	,	0.2648695616	,	0.2802603622	,
0.2958391449	,	0.3116045657	,	0.3275239497	,
0.192500703	,	0.2060825482	,	0.2194793637	,
0.2328857308	,	0.2462978404	,	0.2597162886	,
0.2731387968	,	0.2865663088	,	0.3000000119	,
0.362054775	,	0.3806945366	,	0.4011161804	,
0.4233317229	,	0.4472182348	,	0.4727573078	,
0.4996955555	,	0.5278924121	,	0.5571375069	,
0.3356037894	,	0.3544407268	,	0.3747353789	,
0.3965085843	,	0.4196572555	,	0.4442014024	,
0.4698972311	,	0.4966483944	,	0.5242727513	,
0.3109297072	,	0.3297294971	,	0.349655274	,
0.3707703915	,	0.3929699955	,	0.4162961403	,
0.440545669	,	0.4656361415	,	0.4914325864	,
0.28832102	,	0.3067944507	,	0.3260941931	,
0.3462781021	,	0.3672902874	,	0.3891312495	,
0.4116773714	,	0.4348605989	,	0.4585758567	,
0.2680959648	,	0.285954048	,	0.3043347174	,
0.3232950214	,	0.3427953247	,	0.3628780276	,
0.3834154959	,	0.4043917263	,	0.425715656	,
0.2503195064	,	0.2672531064	,	0.2843907963	,
0.3018343634	,	0.3195339844	,	0.3375418631	,
0.3557721887	,	0.3742227144	,	0.392854991	,
0.2350371702	,	0.2507279105	,	0.2663354022	,
0.2819437593	,	0.2975520985	,	0.3131610844	,
0.3287708995	,	0.3443830197	,	0.3600000143	,
0.423529665	,	0.4447477998	,	0.4680691402	,
0.4934981794	,	0.520885244	,	0.5502015424	,
0.5811485792	,	0.6135602395	,	0.6471912713	,
0.3931370714	,	0.4145794502	,	0.4377569331	,
0.4626713233	,	0.4891974241	,	0.5173524014	,
0.5468493809	,	0.5775740099	,	0.6093137033	,
0.3648060763	,	0.3862012205	,	0.4089545473	,
0.4331044777	,	0.4585250828	,	0.4852603823	,
0.5130713422	,	0.5418600083	,	0.5714685588	,
0.3388881044	,	0.3598983561	,	0.3819272632	,
0.4049938491	,	0.4290306373	,	0.4540343039	,
0.479859042	,	0.5064238545	,	0.5336055301	,
0.3157663708	,	0.3360523848	,	0.3570128021	,
0.378652722	,	0.4009249606	,	0.4238762131	,
0.447356416	,	0.4713454717	,	0.4957362494	,
0.2955438812	,	0.3147393811	,	0.3342477993	,
0.3541134477	,	0.3742785848	,	0.3948024791	,
0.4155842912	,	0.4366201465	,	0.4578640288	,
0.2782872685	,	0.2960140031	,	0.3137285217	,
0.3314415349	,	0.3491537258	,	0.3668653699	,
0.3845763836	,	0.4022874089	,	0.4200000167	,
0.4839221454	,	0.5075710912	,	0.5336248483	,
0.5620908513	,	0.592793904	,	0.6256884054	,
0.6604482185	,	0.6968767536	,	0.7347012807	,
0.4497964243	,	0.4737213777	,	0.4996349953	,
0.5275359756	,	0.5572782551	,	0.5888710539	,
0.6219990503	,	0.6565257656	,	0.6922142431	,
0.4180229248	,	0.4419175416	,	0.4673745955	,
0.4944289721	,	0.5229349302	,	0.5529346786	,
0.5841651039	,	0.6165094231	,	0.6497917057	,
0.3890002162	,	0.4124808269	,	0.4371403841	,
0.4629859426	,	0.4899397232	,	0.5179921265	,
0.5469841179	,	0.5768192483	,	0.6073595821	,
0.3631788912	,	0.3858542535	,	0.4093196716	,
0.4335606251	,	0.458523686	,	0.4842587176	,
0.5105993547	,	0.5375197021	,	0.5648986412	,
0.3406949189	,	0.3621451466	,	0.3839768446	,
0.4062146454	,	0.4287942139	,	0.451782082	,
0.4750656738	,	0.4986385894	,	0.5224479951	,
0.3216389854	,	0.3414261444	,	0.361227732	,
0.3810243172	,	0.4008194953	,	0.4206146761	,
0.440409967	,	0.4602050842	,	0.4800000191	,
0.5428151508	,	0.5687485117	,	0.5973775431	,
0.6286944132	,	0.6625148323	,	0.6987834456	,
0.7371394851	,	0.7773757528	,	0.8191810522	,
0.5051629941	,	0.5314633481	,	0.5599891789	,
0.5907296291	,	0.6235300778	,	0.6583984878	,
0.6949848887	,	0.7331475158	,	0.7726160184	,
0.47014634	,	0.4964657369	,	0.5245290768	,
0.5543730153	,	0.585840189	,	0.6189773165	,
0.6534917922	,	0.6892618173	,	0.7260862968	,
0.4382200097	,	0.4641335722	,	0.4913576223	,
0.5199043087	,	0.54968962	,	0.5807036343	,
0.6127694648	,	0.645785997	,	0.6795954808	,
0.4098742173	,	0.4349426165	,	0.4608819728	,
0.4876869659	,	0.5152978737	,	0.5437733135	,
0.5729267824	,	0.6027343469	,	0.6330577771	,
0.385284652	,	0.4090345656	,	0.4331937495	,
0.4578077326	,	0.4828014175	,	0.5082538167	,
0.5340375712	,	0.5601484879	,	0.5865257585	,
0.3645650362	,	0.3865025224	,	0.4084343285	,
0.4303632151	,	0.4522874007	,	0.4742142791	,
0.4961418907	,	0.5180707312	,	0.5400000215	,
0.6000000238	,	0.6280655481	,	0.6590761863	,
0.6930301635	,	0.7297109774	,	0.7691049302	,
0.8107943168	,	0.8545712729	,	0.9001008868	,
0.5590295875	,	0.5875881114	,	0.6185787099	,
0.6519945802	,	0.6876544715	,	0.7256057012	,
0.7654457336	,	0.8070355899	,	0.8500840772	,
0.5209807663	,	0.5496416141	,	0.5802088968	,
0.6127269382	,	0.6470137258	,	0.6831503022	,
0.7208010417	,	0.7598453323	,	0.8000672655	,
0.4863311428	,	0.5146211367	,	0.5443453467	,
0.5755192004	,	0.6080444735	,	0.6419299374	,
0.6769717147	,	0.7130683578	,	0.7500504538	,
0.4556392223	,	0.4830793155	,	0.5114746556	,
0.5408195942	,	0.5710451811	,	0.6022270052	,
0.6341536758	,	0.6668056847	,	0.7000336422	,
0.4290754512	,	0.4551446199	,	0.4816654483	,
0.5086871211	,	0.53612589	,	0.5640706686	,
0.592378953	,	0.6210493508	,	0.6500168305	,
0.4067861736	,	0.4309379032	,	0.4550896344	,
0.4792413657	,	0.503393097	,	0.5275448283	,
0.5516965596	,	0.5758482909	,	0.6000000238	])


X = numpy.zeros((9,7,11,3))
nval = 9*7*11
X[:,:,:,0] = data[0*nval:1*nval].reshape((9,7,11),order='f')
X[:,:,:,1] = data[1*nval:2*nval].reshape((9,7,11),order='f')
X[:,:,:,2] = data[2*nval:3*nval].reshape((9,7,11),order='f')

for ku in [2,4]:
    for kv in [3,4]:
        for kw in [2,4]:
            for nCtlu in [4,6]:
                for nCtlv in [8]:
                    for nCtlw in [5,7]:
                        print('+'+'-'*78+'+')
                        print(' '*10 + 'Testing Volume with ku=%d, kv=%d, \
kw=%d, nCtlu=%d, nCtlv=%d, nCtlw=%d'%(ku, kv, kw, nCtlu, nCtlv, nCtlw))
                        print('+'+'-'*78+'+')

                        volume = pySpline.Volume(
                            X=X, ku=ku, kv=kv, kw=kw,
                            nCtlu=nCtlu, nCtlv=nCtlv, nCtlw=nCtlw)
                        volume.recompute()
                        run_volume_test(volume)
                        run_project_test(volume)
                        io_test(volume)
