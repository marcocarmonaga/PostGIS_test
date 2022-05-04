--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2 (Ubuntu 14.2-1ubuntu1)
-- Dumped by pg_dump version 14.2 (Ubuntu 14.2-1ubuntu1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry and geography spatial types and functions';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: vectores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vectores (
    id integer NOT NULL,
    name character varying,
    geom public.geometry,
    area numeric,
    centroid public.geometry
);


ALTER TABLE public.vectores OWNER TO postgres;

--
-- Name: vectores_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vectores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vectores_id_seq OWNER TO postgres;

--
-- Name: vectores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vectores_id_seq OWNED BY public.vectores.id;


--
-- Name: vectores id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vectores ALTER COLUMN id SET DEFAULT nextval('public.vectores_id_seq'::regclass);


--
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text) FROM stdin;
\.


--
-- Data for Name: vectores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vectores (id, name, geom, area, centroid) FROM stdin;
\.


--
-- Name: vectores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vectores_id_seq', 1, false);


--
-- Name: vectores vectores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vectores
    ADD CONSTRAINT vectores_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

